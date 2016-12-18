import pickledb
from comment_fetcher import CommentFetcher
from datetime import date

class Database :

    def __init__(self, year1, month1, day1, year2, month2, day2, posts) :
        self.db = pickledb.load('comments.db', False)
        self.setup_db(year1, month1, day1, year2, month2, day2, posts)

    def setup_db(self, year1, month1, day1, year2, month2, day2, posts):
        cf = CommentFetcher()

        trump_set_1 = cf.get_posts_between('politics', date(int(year1), int(month1), int(day1)), date(int(year2), int(month2), int(day2)), int(posts), "trump")
        clinton_set_1 = cf.get_posts_between('politics', date(int(year1), int(month1), int(day1)), date(int(year2), int(month2), int(day2)), int(posts), "clinton")

        self.db.dcreate("{}-{}-{}-{}-{}-{}".format(year1, month1, day1, year2, month2, day2))
        self.db.dadd("{}-{}-{}-{}-{}-{}".format(year1, month1, day1, year2, month2, day2), ("trump", trump_set_1))
        self.db.dadd("{}-{}-{}-{}-{}-{}".format(year1, month1, day1, year2, month2, day2), ("clinton", clinton_set_1))

        self.db.dump()

def main() :
    db = Database()
    db.setup_db()


if __name__ == "__main__" :
    main()