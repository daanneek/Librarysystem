import json
import csv
import tkinter as tk
from pprint import *
class Library:

    def __init__(self):
        self.book_list = []
        self.customer_list = []
        self.book_loans = []


    def import_data(self):
        """Takes a csv and a json file and outputs their contents into lists"""
        with open("FakeNameSet.csv", 'rt', encoding="utf-8-sig", newline='') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.customer_list.append(line)

        with open("booksset1.json") as json_file:
            self.book_list = json.load(json_file)

        with open("loansbackup.json") as json_file:
            Library.book_loans = json.load(json_file)

    def get_customers(self):
        """Returns all information in the customer list."""
        for person in self.customer_list:
            print(person[3])

    def get_loans_list(self):
        """Returns all information in the loans list"""
        print(self.book_loans)
        loanAdministration.save_loans(Library.book_loans)

    @staticmethod
    def get_book_by(something):
        """Search for a book by name, author, or country of origin, returns all available information about the book."""
        for books in Library.book_list:
            if books['title'] == something or books['author'] == something or books['country'] == something:
                print("Book was found! Here is all known information about this book!")
                print(books)
                break
        else:
            print(something + " was not found it does not exist")

    @staticmethod
    def getter():
        something = inp.get()
        Library.get_book_by(something)


    def add_book_to_library(this, author, country, image, language, link, pages, title, year):
        if Library.check_book(title) == False:
            this.book_list.append({"author": author, "country": country, "imageLink": image, "language": language, "link": link, "pages": pages, "title": title, "year": year})
            print("Book was succesfully added")
            Administration.save_library(Library.book_list)
        # else:
        #     print("Book title is already present in the book database!")
    @staticmethod
    def getAddBook():
        author = inp3.get()
        country = inp4.get()
        image = inp5.get()
        language = inp6.get()
        link = inp7.get()
        pages = inp8.get()
        title = inp9.get()
        year = inp10.get()
        window.update()
        Library.add_book_to_library(author, country, image, language, link, pages, title, year)

    def add_customer(self, number, gender, language, name, surname, address, zipcode, email, username, phonenumber):
        """A class that adds a customer to the library's register. This does NOT add the customer to the csv file."""
        self.customer_list.append([number, gender, language, name, surname, address, zipcode, email, username, phonenumber])
        print("Person was added succesfully")
        Administration.save_customers(Library.customer_list)
            # print("add een functie zodat er meerdere personen kunnen zijn")
    @staticmethod
    def getAddCustomer():
        number = inp11.get()
        gender = inp12.get()
        language = inp13.get()
        name = inp14.get()
        surname = inp15.get()
        address = inp16.get()
        zipcode = inp17.get()
        email = inp18.get()
        username = inp19.get()
        phonenumber = inp20.get()
        Library.add_customer(number, gender, language, name, surname, address, zipcode, email, username, phonenumber)

    def check_book(self, title):
        """Takes the title of a book and checks if it exists in the book list."""
        for books in self.book_list:
            if books['title'] == title:
                return True
        else:
            print("Book named " + title +" does not exist(yet)!")

    def check_person(self, name):
        """Takes the name of a customer and checks if the person exists in the customer list."""
        if name in [j for i in self.customer_list for j in i]:
            return True
        else:
            print(name + " does not exist in our database!")

    def check_bookloans(self, title):
        """Takes the title of a book and checks if it exists in the book_loans list."""
        if any(title in books for books in self.book_loans):
            return True
        else:
            return False

    def loan(self, name, title):
        """Loans a book to a person and checks if the person and book exists, weather the book is already loaned out."""
        if self.check_book(title) and self.check_person(name) and not self.check_bookloans(title):
            book = str(title)
            person = str(name)
            loan = [person, book]
            self.book_loans.append(loan)
            print("Loan was added. Customer "+ name + " loaned book " + title + ".")
        else:
            return ("Loan was not added succesfully!")
    @staticmethod
    def getLoan():
        name = inp1.get()
        title = inp2.get()
        Library.loan(name, title)


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
    def save_library(library):
        with open('booksset1.json', 'w') as outfile:
            json.dump(library, outfile)
    @staticmethod
    def backup_library(library):
        with open('bookssetbackup.json', 'w') as outfile:
            json.dump(library, outfile)

    @staticmethod
    def save_customers(customerlist):
        toCSV = customerlist
        with open("FakeNameSet.csv", "w", encoding="utf-8-sig", newline ='') as f:
            writer = csv.writer(f)
            writer.writerows(toCSV)

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
    def save_loans(customerlist):
        with open('loansbackup.json', 'w') as outfile:
            json.dump(customerlist, outfile)





if __name__ == "__main__":

    # Initializing the Library
    Library = Library()
    Library.import_data()
    #Administration.load_customers_from_backup()            # Add this line to read from a backed-up customer list.
    #Administration.load_books_from_backup()                # Add this line to read from a backed-up book list.
    #Administration.load_loans_from_backup()                # Add this line to read from a backed-up loans list.

    # Authors.get_all_authors_books(Library)                 # Puts every author with their respective book in a list, "unknown" authors excluded


    window = tk.Tk()
    window.geometry("2000x300")
    window.title("Public library system!")



    labelgetbookbytitle = tk.Label(window, text="Give the title, author, or country of origin of the book you want to search for:")
    labelgetbookbytitle.grid(row=0, column=0)
    inp = tk.Entry(window)
    inp.grid(row=0, column=1)
    button1 = tk.Button(text="Click to search for this book!", command=lambda: Library.getter(), width = 40 )
    button1.grid(row=0, column=5)

    labelMakeNewLoan = tk.Label(window, text="Give your name and the book you want to loan: ")
    labelMakeNewLoan.grid(row=3, column=0)
    inp1 = tk.Entry(window)
    inp1.grid(row=3, column=1)
    inp2 = tk.Entry(window)
    inp2.grid(row=3, column=2)
    button2 = tk.Button(text="Click to check and confirm your loan.", command=lambda: Library.getLoan(), width=40)
    button2.grid(row=3, column=5)

    labelAddBook = tk.Label(window, text="fill in the necessary information for adding a book.(author, country, image, language, link, pages, title, year)")
    labelAddBook.grid(row=4, column=0)
    inp3 = tk.Entry(window)
    inp3.grid(row=4, column=1)
    inp4 = tk.Entry(window)
    inp4.grid(row=4, column=2)
    inp5 = tk.Entry(window)
    inp5.grid(row=4, column=3)
    inp6 = tk.Entry(window)
    inp6.grid(row=4, column=4)
    inp7 = tk.Entry(window)
    inp7.grid(row=5, column=1)
    inp8 = tk.Entry(window)
    inp8.grid(row=5, column=2)
    inp9 = tk.Entry(window)
    inp9.grid(row=5, column=3)
    inp10 = tk.Entry(window)
    inp10.grid(row=5, column=4)
    button3 = tk.Button(text="Submit book.", command=lambda: Library.getAddBook(), width = 40)
    button3.grid(row=5, column=5)

    labelAddPerson = tk.Label(window, text = "fill in the necessary information for addign a book.(number, gender, language, name, surname, address, zipcode, email, username, phonenumber)")
    labelAddPerson.grid(row=6, column=0)
    inp11 = tk.Entry(window)
    inp11.grid(row=6, column=1)
    inp12 = tk.Entry(window)
    inp12.grid(row=6, column=2)
    inp13 = tk.Entry(window)
    inp13.grid(row=6, column=3)
    inp14 = tk.Entry(window)
    inp14.grid(row=6, column=4)
    inp15 = tk.Entry(window)
    inp15.grid(row=7, column=1)
    inp16 = tk.Entry(window)
    inp16.grid(row=7, column=2)
    inp17 = tk.Entry(window)
    inp17.grid(row=7, column=3)
    inp18 = tk.Entry(window)
    inp18.grid(row=7, column=4)
    inp19 = tk.Entry(window)
    inp19.grid(row=8, column=1)
    inp20 = tk.Entry(window)
    inp20.grid(row=8, column=2)

    button4 = tk.Button(text="Submit person.", command=lambda: Library.getAddCustomer(), width=40)
    button4.grid(row=8, column=5)

    button_all_books = tk.Button(text="Print all book titles in the catalog.", command=lambda: Catalog.get_all_books(), width = 40).grid(row=1, column=5)
    buttonallcustomers = tk.Button(text="Print all names of all customers.", command=lambda: Library.get_customers(), width = 40).grid(row=2, column=5)
    buttonallloans = tk.Button(text="Print all current loans", command=lambda: Library.get_loans_list(), width=40).grid(row=9, column=5)


    window.mainloop()

# Geen duplicate Namen, IETS VAN ID"S, FIX BACKUPS/SAVES, Fix book vinden, persoon vinden, checks