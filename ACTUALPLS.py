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


        with open("loans.json") as json_file:
            Library.book_loans = json.load(json_file)

    def get_customers(self):
        """Returns all information in the customer list."""
        for person in self.customer_list:
            print("Customer's name " + str(person[3]) + ".ID[" + str(person[0]) + "]")

    @staticmethod
    def get_customer_ID(name):
        for person in Library.customer_list:
            if person[3] == str(name):
                print("Customer's name " + person[3] + " " + person[4] + " with ID[" + person[0] + "]")
                break
        else:
            print(name + "was not found! Did you spell your name correctly?")
    @staticmethod
    def getter3():
        something = inp22.get()
        Library.get_customer_ID(something)

    def get_loans_list(self):
        """Returns all information in the loans list"""
        print("List of all book loans, format [Loan ID, Customer ID, Book Title]")
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
        if not Library.check_book(title):
            this.book_list.append({"author": author, "country": country, "imageLink": image, "language": language, "link": link, "pages": pages, "title": title, "year": year})
            print("Book was succesfully added")
            Administration.save_library(Library.book_list)
        else:
            print("Book title is already present in the book database!")

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
        Library.add_book_to_library(author, country, image, language, link, pages, title, year)

    @staticmethod
    def add_customer(number, gender, language, name, surname, address, zipcode, email, username, phonenumber):
        Library.customer_list.append([number, gender, language, name, surname, address, zipcode, email, username, phonenumber])
        print("Person was added succesfully")
        Administration.save_customers(Library.customer_list)

    @staticmethod
    def searchlist(list):
        x = int(max(list)) + 1
        return x

    @staticmethod
    def generateNumber():
        listt = []
        for customers in Library.customer_list:
            x = customers[0]
            listt.append(int(x))
        return Library.searchlist(listt)

    @staticmethod
    def removeCustomer(Id):
        if Library.check_person(Id):
            newlist = [i for i in Library.customer_list if i[0] != str(Id)]
            print("Person with ID: " + Id + " was removed correctly.")
            Library.customer_list = newlist
            Administration.save_customers(newlist)
        else:
            print("ID is not present in the customer register!")

    @staticmethod
    def getter4():
        something = inp23.get()
        Library.removeCustomer(something)

    @staticmethod
    def getAddCustomer():
        number = Library.generateNumber()
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

    def check_person(self, id):
        """Takes the name of a customer and checks if the person exists in the customer list."""
        if str(id) in [j for i in self.customer_list for j in i]:
            return True
        else:
            print("Person with ID: " + id + " does not exist in our database!")

    def check_bookloans(self, title):
        """Takes the title of a book and checks if it exists in the book_loans list."""
        if any(title in books for books in self.book_loans):
            return True
        else:
            return False

    @staticmethod
    def check_id(id):
        if any(id in loans for loans in Library.book_loans):
            return True
        else:
            return False

    @staticmethod
    def generateId():
        Id = 0
        while Library.check_id(Id):
            Id = Id + 1
        else:
            return Id

    def loan(self, ID, title):
        """Loans a book to a person and checks if the person and book exists, weather the book is already loaned out."""
        if self.check_book(title) and self.check_person(ID) and not self.check_bookloans(title):
            book = str(title)
            person = str(ID)
            loanID = Library.generateId()
            loan = [loanID, person, book]
            self.book_loans.append(loan)
            print("Loan was added. Customer " + ID + " loaned book " + title + ".")
        else:
            print("Loan was not added succesfully, the book has already been loaned out!")


    @staticmethod
    def getLoan():
        id = inp1.get()
        title = inp2.get()
        Library.loan(id, title)

    @staticmethod
    def removeLoanById(Id):
        if Library.check_id(Id):
            Library.book_loans = [i for i in Library.book_loans if i[0] != Id]
            return Library.book_loans
        else:
            print("ID is not present in the book loans register!")

    @staticmethod
    def getLoan2():
        ID = inp21.get()
        if ID.isdigit():
            Id = int(ID)
            Library.removeLoanById(Id)
        else:
            print("Input is not a numerical value")

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
    def save_customers(customerlist):
        toCSV = customerlist
        with open("FakeNameSet.csv", "w", encoding="utf-8-sig", newline ='') as f:
            writer = csv.writer(f)
            writer.writerows(toCSV)

    @staticmethod
    def backup_library(library):
        with open('bookssetbackup.json', 'w') as outfile:
            json.dump(library, outfile)
            print("Current book list saved into backup file!")
            
    @staticmethod
    def backup_customers(customerlist):
        toCSV = customerlist
        with open("FakeNameSetbackUp.csv", "w", encoding="utf-8-sig", newline ='') as f:
            writer = csv.writer(f)
            writer.writerows(toCSV)
            print("Current customer list saved into backup file!")

    @staticmethod
    def load_customers_from_backup():
        Library.customer_list = []
        """takes a csv backup file and loads it into customer list."""
        with open('FakeNameSetbackup.csv', 'rt', encoding="utf-8-sig", newline='') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                Library.customer_list.append(line)
            Administration.save_customers(Library.customer_list)
            print("Successfully loaded customer list from backup.")
    @staticmethod
    def load_books_from_backup():
        """takes a json backup file and loads it into the book list"""
        with open("bookssetbackup.json") as json_file:
            Library.book_list = json.load(json_file)
            Administration.backup_library(Library.book_list)
            print("Successfully loaded book list from backup.")
class loanAdministration:
    @staticmethod
    def save_loans(customerlist):
        with open('loans.json', 'w') as outfile:
            json.dump(customerlist, outfile)

    @staticmethod
    def backup_loans(customerlist):
        with open('loans_backup.json', 'w') as outfile:
            json.dump(customerlist, outfile)
            print("Current loans list saved into backup file!")

    @staticmethod
    def load_loans_from_backup():
        """takes a json backup file and loads it into the loans list"""
        with open("loans_backup.json") as json_file:
            Library.book_list = json.load(json_file)
            loanAdministration.save_loans(Library.book_loans)
            print("Successfully loaded loans list from backup.")


if __name__ == "__main__":

    # Initializing the Library
    Library = Library()
    Library.import_data()

######################################################################################################################################
                                                #   GUI   #
######################################################################################################################################


    window = tk.Tk()
    window.geometry("1580x500")
    window.title("Public library system!")
    window.configure(background="gray")

    labelgetbookbytitle = tk.Label(window, text="Give the title, author, or country of origin of the book you want to search for:")
    labelgetbookbytitle.grid(row=0, column=0)
    inp = tk.Entry(window)
    inp.grid(row=0, column=4)
    button1 = tk.Button(text="Click to search for this book!", command=lambda: Library.getter(), width = 40 )
    button1.grid(row=0, column=6)

    labelMakeNewLoan = tk.Label(window, text="Give your customer ID and the book you want to loan: ")
    labelMakeNewLoan.grid(row=3, column=0)
    inp1 = tk.Entry(window)
    inp1.grid(row=3, column=1)
    inp2 = tk.Entry(window)
    inp2.grid(row=3, column=2)
    button2 = tk.Button(text="Click to check and confirm your loan.", command=lambda: Library.getLoan(), width=40)
    button2.grid(row=3, column=6)

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
    button3.grid(row=5, column=6)

    labelAddPerson = tk.Label(window, text = "fill in the necessary information for addign a book.(gender, language, name, surname, address, zipcode, email, username, phonenumber)")
    labelAddPerson.grid(row=6, column=0)
    inp12 = tk.Entry(window)
    inp12.grid(row=6, column=1)
    inp13 = tk.Entry(window)
    inp13.grid(row=6, column=2)
    inp14 = tk.Entry(window)
    inp14.grid(row=6, column=3)
    inp15 = tk.Entry(window)
    inp15.grid(row=6, column=4)
    inp16 = tk.Entry(window)
    inp16.grid(row=7, column=1)
    inp17 = tk.Entry(window)
    inp17.grid(row=7, column=2)
    inp18 = tk.Entry(window)
    inp18.grid(row=7, column=3)
    inp19 = tk.Entry(window)
    inp19.grid(row=7, column=4)
    inp20 = tk.Entry(window)
    inp20.grid(row=8, column=1)

    button4 = tk.Button(text="Submit person.", command=lambda: Library.getAddCustomer(), width=40)
    button4.grid(row=8, column=6)

    inp21=tk.Entry(window)
    inp21.grid(row=10,column = 4)

    button5 = tk.Button(text="Look up your customer id by name.", command=lambda: Library.getter3(), width=40)
    button5.grid(row=14, column=6)

    inp22=tk.Entry(window)
    inp22.grid(row=14,column = 4)

    button6 = tk.Button(text="Remove a customer with their ID.", command=lambda: Library.getter4(), width=40)
    button6.grid(row=15, column=6)

    inp23=tk.Entry(window)
    inp23.grid(row=15,column = 4)

    buttonremoveloans = tk.Button(text="Remove a loan with its given ID", command=lambda: Library.getLoan2(), width=40).grid(row=10, column=6)
    button_all_books = tk.Button(text="Print all book titles in the catalog.", command=lambda: Catalog.get_all_books(), width = 40).grid(row=1, column=6)
    buttonallcustomers = tk.Button(text="Print names and id's of all customers.", command=lambda: Library.get_customers(), width = 40).grid(row=2, column=6)
    buttonallloans = tk.Button(text="Print all current loans", command=lambda: Library.get_loans_list(), width=40).grid(row=9, column=6, padx =(20,20))
    buttonbackupcostumers = tk.Button(text="Backup the customer list into a seperate file.", command=lambda: Administration.backup_customers(Library.customer_list), width = 40).grid(row=11, column=6)
    buttonbackupbooks = tk.Button(text="Backup the books list into a seperate file.", command=lambda: Administration.backup_library(Library.book_list), width = 40).grid(row=12, column=6)
    buttonloans = tk.Button(text="Backup the loans list into a seperate file.", command=lambda: loanAdministration.backup_loans(Library.book_loans), width = 40).grid(row=13, column=6)
    buttonloadcostumers = tk.Button(text="Load a backup file as the customer list.", command=lambda: Administration.load_customers_from_backup(), width = 40).grid(row=16, column=6)
    buttonloadupbooks = tk.Button(text="Load a backup file as the book list.", command=lambda: Administration.load_books_from_backup(), width = 40).grid(row=17, column=6)
    buttonloadloans = tk.Button(text="Load a backup file as the loan list.", command=lambda: loanAdministration.load_loans_from_backup(), width = 40).grid(row=18, column=6)
    window.mainloop()