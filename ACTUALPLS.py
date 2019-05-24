import json
import csv


class Library:

    def __init__(this):
        this.book_list = []
        this.customer_list = []
        this.book_loans = []

    def import_data(this):
        """Takes a csv and a json file and outputs their contents into lists"""
        with open('FakeNameSet.csv', 'rt', encoding="utf-8-sig", newline='') as f:
            csv_reader = csv.reader(f)
            row1 = next(csv_reader)
            del row1
            for line in csv_reader:
                this.customer_list.append(line)

        with open('booksset1.json') as json_file:
            this.book_list = json.load(json_file)

    def display_customer_list(this):
        print(this.customer_list)

    def get_book_by_title(this, title):
        """Takes a book's title and returns all available information about the book."""
        for book in  this.book_list:
            if book['title'] == title:
                print (book)

    def get_book_by_author(this, author):
        """Takes an author's name as input and returns all available information about the book."""
        for book in  this._book_list:
            if book['author'] == author:
                print (book)

    def check(this, title):
        """Takes the title of a book and checks if it exists in the book list."""
        for books in this.book_list:
            if books['title'] == title:
                return True

    def backup_library(self,library):
        with open('bookssetbackup.json', 'w') as outfile:
            json.dump(library, outfile)

    def backup_customers(self, customerlist):
        toCSV = customerlist
        with open("FakeNameSetbackUp.csv", "w", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerows(toCSV)

    def backup_loans(self, customerlist):
        with open('loansbackup.json', 'w') as outfile:
            json.dump(customerlist, outfile)

    def check_person(this, name):
        """Takes the name of a customer and checks if the person exists in the customer list."""
        if name in [j for i in this.customer_list for j in i]:
            return True

    def check_bookloans(this, title):
        """Takes the title of a book and checks if it exists in the book_loans list."""
        if any(title in sl for sl in this.book_loans):
            return True
        else:
            return False

    def add_book_to_library(this, new_book):
        """Takes the necessary information for a book and adds it to the book_list, not to the backup json file."""
        this.book_list.append(new_book)

    def add_customer(self, new_customer):
        """A class that adds a customer to the library's register. NOTE this does NOT add the customer to the csv file."""
        lib1.customer_list.append(new_customer)

    def loan(this, name, title):
        """Loans a book to a person and checks if the person and book exists, weather the book is already loaned out."""
        if lib1.check(title) and lib1.check_person(name) and not this.book_loans:
            book = str(title)
            person = str(name)
            loan = [person, book]
            this.book_loans.append(loan)
        else:
            if lib1.check(title) and lib1.check_person(name) and not lib1.check_bookloans(title):
                book = str(title)
                person = str(name)
                loan = [person, book]
                this.book_loans.append(loan)


if __name__ == "__main__":
    lib1 = Library()
    lib1.import_data()

    lib1.loan("Hisham", 'Pride and Prejudice')
    lib1.loan("Hisham", 'Things Fall Apart')
    lib1.loan("Rodin", 'The Sound of the Mountain')            #if a person does not exist the loan does not get added,
    lib1.loan("Maren", 'Berlin Alexanderplatz')                #if a book gets added that doesn't exist neither.
    lib1.loan("Rodin", 'Berlin Alexanderplatz')                #if a book that is already loaned out gets loaned again,
    lib1.loan("Hisham", "REEEEEE")                             #it does not show up in the bookloans list.
    #print(lib1.book_loans)

    lib1.check_bookloans('Berlin Alexanderplatz')
    lib1.check_bookloans("REEEEEE")

    #lib1.get_book_by_title("The Sound of the Mountain")
    lib1.add_book_to_library({"author": "TstAuthor","country": "TestCountry","imageLink": "images/TestImage","language": "TestLanguage","link": "Testlink\n","pages": 1,"title": "No","year": 1836})
    lib1.backup_library(lib1.book_list)
    lib1.add_customer(['21',  'male',  'Dutch',  'Daan',  'Nekeman',  'Straat 1',  '9461 JE',  'Gieten',  'GulserenWilligenburg@teleworm.us',  'Ressoare',  '06-92433659'])
    lib1.backup_customers(lib1.customer_list)
    lib1.backup_loans(lib1.book_loans)




