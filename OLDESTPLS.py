import json
import csv
from collections import OrderedDict
import pprint

class Library:
    """Creates a library with a list of books, imported from the booksset1.json json file, or any other file given in name == main"""
    def __init__(self, book_list):
        self._book_list = book_list


    def get_book_by_title(self, title):
        """"Searches the library's dictionary for a book by its given title."""
        for book in  self._book_list:
            if book['title'] == title:
                print (book)


    def get_book_by_author(self, author):
        """"Searches the library's dictionary for a book by its given author."""
        for book in  self._book_list:
            if book['author'] == author:
                print (book)


    def get_all_authors(self):
        """Searches the dictionary and prints the names of all the authors."""
        authors = [x["author"] for x in self._book_list]
        print(authors)


    def add_book_to_library(self, new_book):
        """A class that adds a book to the library's dictionary. NOTE this does NOT add the book to the Json file."""
        self._book_list.append(new_book)

    def move_rented_book(self,title):
        for book in range(len(booklist)-1):
            if booklist[book]['title'] == title:
                del booklist[book]

    def backup_library(self,library):
        with open('bookssetbackup.json', 'w') as outfile:
            json.dump(library, outfile)


class catalog(Library):
    @staticmethod
    def get_all_books():
        """A method that displays ALL books in the dictionary of the library class."""
        for book in booklist:
            print(book['title'])

class CustomerAdministration(Library):
    """ A class that handles all the customers, adds them to the customer_list from a csv file and handles renting out books."""
    def __init__(self, customer_list):
        self.customer_list = []

    def add_customer(self, new_customer):
        """A class that adds a customer to the library's register. NOTE this does NOT add the customer to the csv file."""
        customer_list.append(new_customer)

    @staticmethod
    def backup_customers():
        toCSV = customer_list
        with open("FakeNameSetbackUp.csv", "w", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerows(toCSV)

class authors(CustomerAdministration):
    books = []
    def __init__(self,name,books):
        self.name = name
        self.books = books
    @staticmethod
    def get_name(self):
        print(self.name)
    @staticmethod
    def get_titles(self):
        print(self.books)


class loanbooks(CustomerAdministration, Library):
    def __init(self):
        self.bookloans = []

    def rent_book(person, title):
        bookloans = []
        if person in customer_list[0:]:
            if title in booklist:
                x = str(person)
                y = str(title)
                a = {x: y}
                bookloans.append(dict(a))

        print(bookloans) # > {Person, book}


if __name__ =="__main__":
    with open('booksset1.json') as json_file:                                   #To load backup, change json to bookssetbackup.json
        booklist = json.load(json_file)
    library = Library(booklist)

    with open('FakeNameSet.csv', 'rt', encoding="utf-8-sig",newline = '') as f: #To load backup, change csv to FakeNameSetbackUp.csv
        csv_reader = csv.reader(f)
        customer_list = []
        for line in csv_reader:
            customer_list.append(line)
        customerlist = CustomerAdministration(customer_list)


    #library.get_book_by_author('TestAuthor') #Searching for a book (By author).
    #library.get_book_by_title('Fairy tales') #Searching for a book (By title).
    loanbooks.rent_book("Bengt","The Decameron") #Making a book loan for an available book item.
    #customerlist.add_customer(['21',  'male',  'Dutch',  'Daan',  'Nekeman',  'Straat 1',  '9461 JE',  'Gieten',  'GulserenWilligenburg@teleworm.us',  'Ressoare',  '06-92433659']) #Adding new customers.
    #customerlist.add_customer(['22',  'male',  'Dutch',  'Danyel',  'Fijten',  'Straat 2',  '9461 JE',  'Gieten',  'GulserenWilligenburg@teleworm.us',  'Ressoare',  '06-92433659'])
    #customerlist.add_customer(['23',  'male',  'Dutch',  'Wouter',  'van der Schoot',  'Straat 3',  '9461 JE',  'Gieten',  'GulserenWilligenburg@teleworm.us',  'Ressoare',  '06-92433659'])
    #library.add_book_to_library({"author": "TstAuthor","country": "TestCountry","imageLink": "images/TestImage","language": "TestLanguage","link": "Testlink\n","pages": 1,"title": "No","year": 1836})#Adds a book to library instance #Adding new book.
    #CustomerAdministration.backup_customers() #backup all people currently in the customer list to a csv file
    #Library.backup_library(library, booklist) #backups the instance of library to the file bookssetbackup.json included in the assignment.
    #catalog.get_all_books() # Prints all titles
    #author1 = authors("Danyel",["how2sD","DanyelBiography"]) #Create new author with name and titles
    #authors.get_name(author1) #Get author name
    #authors.get_titles(author1) #Get author titles