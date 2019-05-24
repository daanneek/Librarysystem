Simple library system, by Danyel(0964776) ,Daan(0977498) and Wouter(0977531).

We decided to keep it as simple as it can be, with minimal classes.
We created a central class called Library and made a few classes that support this main class.
the classes that support the central class are:
- loanbooks, creates a list which houses books and the people that have lend them.
- Catalog, shows all books currently available in the library
- CustomerAdministration, keeps track of customers, can search for certain customers, create new customers.	
  and backup the customer list into a csv file.
- authors, creates and lists author's names and the books they've written.
  Library is the central class which contains functions to search by books by author name and title, backup the book list, and add books to a library.


Most classes in the code have explanation above them, and when they're called at the bottom of the file.
All requirements for the Assignment are done by calls at the bottom of the file. There are more functions in the system,but calling them is not required for the assesment of the assignment.


Included Files;
README.txt
booksset1.json; the original booksset from the assignment.
bookssetbackup.json; the backup file for the books, can be deleted and will be remade by the backup function.
FakeNameSet.csv; the originial fake nameset from the assignment.
FakeNameSetbackUp.csv; the backup file for the customers, can be deleted andw will be remade by the backup function.
loansbackup.json; gives a file with all current loans.
PLS.py; main python file.
Class Diagram.pdf