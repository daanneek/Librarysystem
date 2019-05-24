import json
import csv

if __name__ =="__main__":
    with open('booksset1.json') as json_file:
        booklist = json.load(json_file)




title = "Berlin Alexanderplatz"
bookloans = [['Hisham', 'Things Fall Apart'], ['Hisham', 'Pride and Prejudice'], ['Hisham', 'Berlin Alexanderplatz']]


def check_bookloans(title):
    if any(title in sl for sl in bookloans) == True:
        print("True")
        return True
    else:
        print("False")
        return False


check_bookloans('Pride and Prejudice')
check_bookloans('Pride and Prejudice')
check_bookloans('Berlin Alexanderplatz')
check_bookloans('daan')