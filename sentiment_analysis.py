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

class SentimentAnalysis :

    WORD_LENGTH_THRESHOLD = 3

    def __init__(self):
        print("Downloading required nltk dependencies...")
        nltk.download('punkt')

        if os.path.isfile('trained_classifier.pickle') :
            print("Classifier already trained, loading file...")
            file = open("trained_classifier.pickle", "rb")
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

    def classify(self, statement):
        return self.classifier.classify(self.get_features_in_statement(statement))

def main() :
    sa = SentimentAnalysis()

    print("Testing classifier with sentence 'I love dogs'")
    print(sa.classify("I love dogs"))

    print("Testing classifier with sentence 'I hate dogs'")
    print(sa.classify("I hate dogs"))


if __name__ == "__main__" :
    main()