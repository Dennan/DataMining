from database import Database
from sentiment_analysis import SentimentAnalysis

def main() :
    sa = SentimentAnalysis()

    db = Database()
    trump_comments = db.db.get('2016-10-1-2016-11-1').get("trump")
    clinton_comments = db.db.get('2016-10-1-2016-11-1').get("clinton")

    trump_score = 0
    clinton_score = 0

    for comment in trump_comments :
        print("Testing classifier with sentence :", comment)
        result = sa.classify(comment)
        print(result)
        if result == "positive" :
            trump_score = trump_score + 1
        elif result == "negative" :
            trump_score = trump_score - 1

    for comment in clinton_comments :
        print("Testing classifier with sentence :", comment)
        result = sa.classify(comment)
        print(result)
        if result == "positive" :
            clinton_score = clinton_score + 1
        elif result == "negative" :
            clinton_score = clinton_score - 1

    if clinton_score > trump_score :
        print("Hilary Clinton has greater support than Donald Trump, at ",clinton_score," to ",trump_score,".")
    elif trump_score > clinton_score :
        print("Donald Trump has greater support than Hilary Clinton, at ",trump_score," to ",clinton_score,".")
    else :
        print("Hilary Clinton and Donald Trump have the same support, at ",clinton_score," and ",trump_score," each.")

if __name__ == "__main__" :
    main()