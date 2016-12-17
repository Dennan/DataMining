'''
Sentiment analysis using a Naive Bayesian classifier.
The statements are analyzed word by word, and each word is deemed to be a positive or negative word.

Some edge cases will be incorrectly deemed positive when they are negative or vice versa, but this error should be less severe
with a large enough data set.

Words that are too short are not counted - this catches things like "and", "or", "I", etc which are neither positive or negative.

Potential improvements to this algorithm could be to look at sets of word multiple words at a time. This would require a larger and more diverse
training data set.
'''


import nltk
import os
import pickle
from comment_fetcher import CommentFetcher
from datetime import date

class SentimentAnalysis :

    WORD_LENGTH_THRESHOLD = 3
    NEUTRAL_THRESHOLD = 0.1

    def __init__(self):
        print("Downloading required nltk dependencies...")
        nltk.download('punkt')

        if os.path.isfile('trained_bayesian_classifier.pickle') :
            print("Classifier already trained, loading file...")
            file = open("trained_bayesian_classifier.pickle", "rb")
            self.classifier, self.features = pickle.load(file)
            file.close()
        else :
            print("No classifier file found, training classifier and saving...")
            self.train()
            file = open("trained_classifier.pickle", "wb")
            pickle.dump((self.classifier, self.features), file)
            file.close()

    def train(self):
        positive_examples = []
        negative_examples = []
        positive_file = open("positive_training.txt", "r")
        negative_file = open("negative_training.txt", "r")

        for line in positive_file :
            positive_examples.append(line.replace("\n", ""))

        for line in negative_file :
            negative_examples.append(line.replace("\n", ""))

        all_words = []

        for example in positive_examples + negative_examples :
            words = [word.lower() for word in example.split() if len(word) >= self.WORD_LENGTH_THRESHOLD]
            all_words.extend(words)

        all_words_dist = nltk.FreqDist(all_words)
        self.features = list(all_words_dist.keys())

        featuresets = []
        for statement in positive_examples :
            featuresets.append((self.get_features_in_statement(statement), "positive"))

        for statement in negative_examples :
            featuresets.append((self.get_features_in_statement(statement), "negative"))

        self.classifier = nltk.NaiveBayesClassifier.train(featuresets)

    def get_features_in_statement(self, statement):
        word_set = set(statement.split())
        features = {}

        for word in self.features :
            features[word] = (word in word_set)

        return features

    # returns strings "positive", "negative", or "neutral"
    # note: "neutral" doesn't necessarily mean that the comment is neutral, it just means that
    # we don't have enough information to classify it as either positive or negative
    def classify(self, statement):
        prob_dist = self.classifier.prob_classify(self.get_features_in_statement(statement))

        if (abs(prob_dist.prob(prob_dist.max())) - 0.5 ) < self.NEUTRAL_THRESHOLD :
            return "neutral"
        else :
            return self.classifier.classify(self.get_features_in_statement(statement))

def create_training_files() :
    cf = CommentFetcher()
    start_date = date(2014, 1, 1)
    end_date = date(2014, 4, 1)

    comments = cf.get_posts_between('politics', start_date, end_date, 5, 'opinion')

    pos_file = open("positive_training.txt", "a")
    neg_file = open("negative_training.txt", "a")

    for comment in comments :
        print(comment)
        choice = input("p, n or x(not applicable), q for quit(important if you want to save!)? : ")

        if choice == 'p' :
            pos_file.write(comment + "\n")
        elif choice =='n' :
            neg_file.write(comment + "\n")
        elif choice == 'q' :
            break

    pos_file.close()
    neg_file.close()

def main() :
    sa = SentimentAnalysis()

    print("Testing classifier with sentence 'I love dogs'")
    print(sa.classify("I love dogs"))

    print("Testing classifier with sentence 'I hate dogs'")
    print(sa.classify("I hate dogs"))

    print("Testing classifier with sentence 'omlettes'")
    print(sa.classify("omlettes"))

    print("Testing classifier with sentence 'I like dogs'")
    print(sa.classify("I like dogs"))

    create_training_files()

if __name__ == "__main__" :
    main()