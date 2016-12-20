from db_analysis import dbAnalysis

def main() :

    toggle = input('Would you like to use a custom date? (y): ')

    if toggle == "y":
        year1 = input('Input the start year (XXXX): ')
        month1 = input('Input the start month (XX): ')
        day1 = input('Input the start day (XX): ')
        year2 = input('Input the end year (XXXX): ')
        month2 = input('Input the end month (XX): ')
        day2 = input('Input the end day (XX): ')
        posts = input('Input the maximum amount of posts you would like to look at: ')
        dbAnalysis(year1, month1, day1, year2, month2, day2, posts)

    else :
        print("\nWhen Trump announces his candidacy for president: June 16, 2015")
        dbAnalysis('2015', '6', '16', '2015', '6', '23', '5')

        print("When Trump is named the Republican Candidate: May 3, 2016")
        dbAnalysis('2016', '5', '3', '2016', '5', '10', '5')

        print("When Clinton is named the Democratic Candidate: July 26, 2016")
        dbAnalysis('2016', '7', '26', '2016', '8', '2', '5')

        print("When Clinton makes a comment about \"Deplorables\": September 9, 2016")
        dbAnalysis('2016', '9', '9', '2016', '9', '16', '5')

        print("Presidential Debate #1: September 26, 2016")
        dbAnalysis('2016', '9', '26', '2016', '10', '3', '5')

        print("Video of Trump making sexist comments released: October 7, 2016")
        dbAnalysis('2016', '10', '7', '2016', '10', '14', '5')

        print("Presidential Debate #2: October 9, 2016")
        dbAnalysis('2016', '10', '9', '2016', '10', '16', '5')

        print("Presidential Debate #3: October 19, 2016")
        dbAnalysis('2016', '10', '19', '2016', '10', '26', '5')

        print("FBI reopen Clinton Email Investigation: October 28, 2016")
        dbAnalysis('2016', '10', '28', '2016', '11', '4', '5')

        print("FBI close Clinton Email Investigation, no charges against Clinton: Nov 7, 2016")
        dbAnalysis('2016', '11', '7', '2016', '11', '14', '5')

        print("Election Day: November 8, 2016")
        dbAnalysis('2016', '11', '8', '2016', '11', '15', '5')


if __name__ == "__main__" :
    main()