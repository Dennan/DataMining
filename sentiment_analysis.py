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


class SentimentAnalysis :

    WORD_LENGTH_THRESHOLD = 3

    def __init__(self):
        print("Downloading required nltk dependencies...")
        nltk.download('punkt')

    def train(self):
        positive_examples = ['I love this politician',
                             'Everything is great',
                             'I love everything']

        negative_examples = ['I hate this politican',
                             'Everything is terrible',
                             'I hate everything']

        word_lists = []
        # convert to lists of significant words

        for words in positive_examples :
            words = [word.lower() for word in words.split() if len(word) >= self.WORD_LENGTH_THRESHOLD]
            word_lists.append((words, 'positive'))

        for words in negative_examples :
            words = [word.lower() for word in words.split() if len(word) >= self.WORD_LENGTH_THRESHOLD]
            word_lists.append((words, 'negative'))


        all_words = []
        for tuple in word_lists :
            all_words.extend(tuple[0])

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
    sa.train()

    print("Testing classifier with sentence 'I love dogs'")
    print(sa.classify("I love dogs"))

    print("Testing classifier with sentence 'I hate dogs'")
    print(sa.classify("I hate dogs"))


if __name__ == "__main__" :
    main()