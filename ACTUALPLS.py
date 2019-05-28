import json
import csv

class Library:

    def __init__(self):
        self.book_list = []
        self.customer_list = []
        self.book_loans = []


    def import_data(self):
        """Takes a csv and a json file and outputs their contents into lists"""
        with open("FakeNameSet.csv", 'rt', encoding="utf-8-sig", newline='') as f:
            csv_reader = csv.reader(f)
            row1 = next(csv_reader)
            del row1
            for line in csv_reader:
                self.customer_list.append(line)

        with open("booksset1.json") as json_file:
            self.book_list = json.load(json_file)

    def get_customer_list(self):
        """Returns all information in the customer list."""
        print(self.customer_list)

    def get_book_list(self):
        """Returns all information in the book list"""
        print(self.book_list)

    def get_loans_list(self):
        """Returns all information in the loans list"""
        print(self.book_loans)

    def get_book_by(this, something):
        """Search for a book by name, author, or country of origin, returns all available information about the book."""
        for books in this.book_list:
            if books['title'] == something or books['author'] == something or books['country'] == something:
                print(books)

    def get_book_by_title(this, title):
        """Takes a book's title and returns all available information about the book."""
        for book in this.book_list:
            if book['title'] == title:
                print(book)

    def get_book_by_author(self, author):
        """Takes an author's name as input and returns all available information about the book."""
        for book in self.book_list:
            if book['author'] == author:
                print(book)

    def add_book_to_library(self, new_book):
        """Takes the necessary information for a book and adds it to the book_list, not to the backup json file."""
        self.book_list.append(new_book)

    def add_customer(self, new_customer):
        """A class that adds a customer to the library's register. This does NOT add the customer to the csv file."""
        Library.customer_list.append(new_customer)

    def check_book(self, title):
        """Takes the title of a book and checks if it exists in the book list."""
        for books in self.book_list:
            if books['title'] == title:
                return True

    def check_person(self, name):
        """Takes the name of a customer and checks if the person exists in the customer list."""
        if name in [j for i in self.customer_list for j in i]:
            return True

    def check_bookloans(self, title):
        """Takes the title of a book and checks if it exists in the book_loans list."""
        if any(title in books for books in self.book_loans):
            return True
        else:
            return False

    def loan(self, name, title):
        """Loans a book to a person and checks if the person and book exists, weather the book is already loaned out."""
        if self.check_book(title) and self.check_person(name) and not self.book_loans:
            book = str(title)
            person = str(name)
            loan = [person, book]
            self.book_loans.append(loan)
        else:
            if Library.check_book(title) and Library.check_person(name) and not Library.check_bookloans(title):
                book = str(title)
                person = str(name)
                loan = [person, book]
                self.book_loans.append(loan)


class Catalog(Library):
    @staticmethod
    def get_all_books():
        """A method that displays ALL book titles available in the library, could be loaned out."""
        for book in Library.book_list:
            print(book['title'])


class Authors():
    @staticmethod
    def get_all_authors_books(library):
        """A method that displays ALL authors and their books available in the library, without duplicates/unknown."""
        author_list = []
        for author in library.book_list:
            if author['author'] != 'Unknown':
                author_list.append((author['author'], author['title']))
        print(list(dict(dict.fromkeys(author_list))))


class Administration(Library):
    """Class administration goes over the saving of the parts of the library system."""
    @staticmethod
    def backup_library(library):
        with open('bookssetbackup.json', 'w') as outfile:
            json.dump(library, outfile)

    @staticmethod
    def backup_customers(customerlist):
        toCSV = customerlist
        with open("FakeNameSetbackUp.csv", "w", encoding="utf-8-sig", newline ='') as f:
            writer = csv.writer(f)
            writer.writerows(toCSV)

    @staticmethod
    def load_customers_from_backup():
        """takes a csv backup file and loads it into customer list."""
        with open('FakeNameSetbackup.csv', 'rt', encoding="utf-8-sig", newline='') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                Library.customer_list.append(line)

    @staticmethod
    def load_books_from_backup():
        """takes a json backup file and loads it into the book list"""
        with open("bookssetbackup.json") as json_file:
            Library.book_list = json.load(json_file)


class loanAdministration:
    @staticmethod
    def backup_loans(customerlist):
        with open('loansbackup.json', 'w') as outfile:
            json.dump(customerlist, outfile)

    @staticmethod
    def load_loans_from_backup():
        """Takes a json backup file and loads it into the book loans list"""
        with open("loansbackup.json") as json_file:
            Library.book_loans = json.load(json_file)

if __name__ == "__main__":

    # Initializing the Library
    Library = Library()
    Library.import_data()
    #Administration.load_customers_from_backup()            # Add this line to read from a backed-up customer list.
    #Administration.load_books_from_backup()                # Add this line to read from a backed-up book list.
    #Administration.load_loans_from_backup()                # Add this line to read from a backed-up loans list.

    # Adding loans to a loaned books list, if a person does not exist the loan does not get added, if a book gets added
    # that doesn't exist neither. If a book that is loaned out gets loaned, it does not show up in the book_loans list.
    #Authors.get_all_authors_books(Library)                 # Puts every author with their respective book in a list, "unknown" authors excluded
    Library.loan("Hisham", 'Pride and Prejudice')
    Library.loan("Hisham", 'Things Fall Apart')
    Library.loan("Rodin", 'The Sound of the Mountain')
    Library.loan("Rodin", 'Berlin Alexanderplatz')
    Library.loan("Hisham", "REEEEEE")
    Library.loan("Maren", 'Sentimental Education')
    #Library.get_book_by("Jane Austen")
    #Library.get_book_by("Berlin Alexanderplatz")   # prints available information for a book
    #Library.get_customer_list()                    # prints all customers in the customer administration
    #Catalog.get_all_books()                        # Prints all book titles in the Library

    #lib1.get_book_by_title("The Sound of the Mountain")
    Library.add_book_to_library({"author": "TstAuthor", "country": "TestCountry", "imageLink": "images/TestImage", "language": "TestLanguage", "link": "Testlink\n", "pages": 1, "title": "No", "year": 1836})
    Administration.backup_library(Library.book_list)
    Library.add_customer(['21', 'male', 'Dutch', 'Daan', 'Nekeman', 'Straat 1', '9461 JE', 'Gieten', 'GulserenWilligenburg@teleworm.us', 'Ressoare', '06-92433659'])
    Administration.backup_customers(Library.customer_list)
    loanAdministration.backup_loans(Library.book_loans)



