from database import Database
from sentiment_analysis import SentimentAnalysis
import re

class dbAnalysis :
    sa = SentimentAnalysis()
    def __init__(self, year1, month1, day1, year2, month2, day2, posts):

        db = Database(year1, month1, day1, year2, month2, day2, posts)
        trump_comments = db.db.get("{}-{}-{}-{}-{}-{}".format(year1, month1, day1, year2, month2, day2)).get("trump")
        clinton_comments = db.db.get("{}-{}-{}-{}-{}-{}".format(year1, month1, day1, year2, month2, day2)).get("clinton")

        trump_score = 0
        clinton_score = 0

        for comment in trump_comments :
            #print("Testing classifier with sentence :", comment)
            result = self.sa.classify(comment)
            #print(result)
            if result == "positive" :
                if re.search(' /s ', comment, 0) == None :
                    trump_score = trump_score + 1
                else :
                    trump_score = trump_score - 1
            elif result == "negative" :
                if re.search(' /s ', comment, 0) == None :
                    trump_score = trump_score - 1
                else :
                    trump_score = trump_score + 1

        for comment in clinton_comments :
            #print("Testing classifier with sentence :", comment)
            result = self.sa.classify(comment)
            #print(result)
            if result == "positive" :
                if re.search('/s', comment, 0) == None :
                    clinton_score = clinton_score + 1
                else :
                    clinton_score = clinton_score - 1
            elif result == "negative" :
                if re.search('/s', comment, 0) == None :
                    clinton_score = clinton_score - 1
                else :
                    clinton_score = clinton_score + 1

        if clinton_score > trump_score :
            print("Hillary Clinton has greater support than Donald Trump, at {} to {}.\n".format(str(clinton_score), str(trump_score)))
        elif trump_score > clinton_score :
            print("Donald Trump has greater support than Hillary Clinton, at {} to {}.\n".format(str(trump_score), str(clinton_score)))
        else :
            print("Hillary Clinton and Donald Trump have the same support, at {} and {} each.\n".format(str(clinton_score), str(trump_score)))

def main() :
    year1 = input('Input the start year (XXXX): ')
    month1 = input('Input the start month (XX): ')
    day1 = input('Input the start day (XX): ')
    year2 = input('Input the end year (XXXX): ')
    month2 = input('Input the end month (XX): ')
    day2 = input('Input the end day (XX): ')
    posts = input('Input the maximum amount of posts you would like to look at: ')
    analysis = dbAnalysis(year1, month1, day1, year2, month2, day2, posts)

if __name__ == "__main__" :
    main()