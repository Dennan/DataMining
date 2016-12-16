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

        all_words = set(word.lower() for statement in positive_examples for word in nltk.tokenize.word_tokenize(statement))

        print(all_words)
        print(word_lists)



def main() :
    SentimentAnalysis().train()

if __name__ == "__main__" :
    main()