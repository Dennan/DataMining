import pickledb
from comment_fetcher import CommentFetcher
from datetime import date

CURRENT_DATA_VERSION = "0.01"

class Database :

    def __init__(self) :
        self.db = pickledb.load('comments.db', False)
        if self.db.get("version") != CURRENT_DATA_VERSION :
            self.setup_db()

    def setup_db(self):
        self.db.deldb()
        self.db.set("version", CURRENT_DATA_VERSION)

        cf = CommentFetcher()

        trump_set_1 = cf.get_posts_between('politics', date(2016, 10, 1), date(2016, 11, 1), 10, "trump")
        clinton_set_1 = cf.get_posts_between('politics', date(2016, 10, 1), date(2016, 11, 1), 10, "clinton")

        self.db.dcreate("2016-10-1-2016-11-1")
        self.db.dadd("2016-10-1-2016-11-1", ("trump", trump_set_1))
        self.db.dadd("2016-10-1-2016-11-1", ("clinton", clinton_set_1))

        self.db.dump()

def main() :
    db = Database()
if __name__ == "__main__" :
    main()