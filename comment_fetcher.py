# Calls the Reddit API to fetch posts with given parameters.

import praw
import time
from datetime import datetime, date, timedelta

class CommentFetcher :
    def __init__(self):
        self.reddit = praw.Reddit(client_id='-XI9UfmWIHi5-w',
                             client_secret='V5gl1COg1TzNZIe6D7ilvbzz75A',
                             password='datamining', # shh, don't tell anyone
                             username='dataminingthrowaway',
                             user_agent='python script')

    # gets posts from a given subreddit between start_date and end_date
    def get_posts_between(self, subreddit, start_date, end_date, max_posts, keywords):
        print("Fetching comments from {} submissions on /r/{} between {} and {}, with titles containing keywords [{}]\n".format(max_posts, subreddit, start_date, end_date, keywords))

        start_timestamp = time.mktime(start_date.timetuple())
        end_timestamp = time.mktime(end_date.timetuple())

        query = "(and timestamp:{}..{} title:'{}')".format(int(start_timestamp), int(end_timestamp), keywords)
        sr = self.reddit.subreddit(subreddit)
        results = sr.search(query, sort='top', syntax='cloudsearch', limit=max_posts)

        all_comments = []
        for submission in results :
            submission.comments.replace_more(limit=0)
            new_comments = [comment.body for comment in submission.comments]
            all_comments = all_comments + new_comments

        return all_comments


def main() :
    # sample usage
    fetcher = CommentFetcher()
    start_date = date(2016, 7, 1)
    end_date = date(2016, 8, 1)


    print(fetcher.get_posts_between('politics', start_date, end_date, 5, "trump"))


if __name__ == "__main__" :
    main()

