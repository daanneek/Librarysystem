Simple library system, by Danyel(0964776) ,Daan(0977498) and Wouter(0977531).

!!! OUTPUT IS GIVEN IN CONSOLE NOT IN THE GUI PART!!!

The system should save after you add or remove loans, books and people. It also has a manual backup functions in lines 11,12,13 and 17,18,19.

If everything goes well, when you execute the ACTUALPLS.py program it should spawn a GUI with alot of buttons and fields. Underneath we will provide explaination about every button and field.
From top to bottom; from left to right;

1. First field takes a book title and "Click to search for this book" returns all information known about that book.
2. "Print all book titles in the catalog" prints out all the titles in the Library.
3. "Print names and id's of all customers" prints all first and seconds names in the system with their corresponding ID.
4. First field takes customer ID, second field takes a book title, "click to check and confirm your loan" checks if book exists, ID exists and if True adds the book to the book_loan list.
5/6. Fields take the input given in the description in the UI. "submit book" adds it to the book_list.
7/8/9. Fields take the input given in the description in the UI, "submit person" adds it to the customer_list and gives the person a unique ID.
10. "print all current loans" prints the loan list, with format Loan ID, Customer ID and book title.
11. field takes a loan ID and "remove a loan with its given ID." removes the loan from the loan_list.
12. "Backup the customer list into a seperate file" backup's the customer list into the FakeNameSetBackUp.csv file, line 17 loads this backup.
13. "Backup the books list into a seperate file" backup's the book list into the bookssetbackup.json file, line 18 loads this backup.
14. "Backup the loans list into a seperate file" backup's the book list into the loans_backup.json file, line 19 loads this backup.
15. Field takes name and returns the id of the customer.
16. Field takes an ID and removes that person from the customer_List.
17. Button loads a backup from the customer_list saved with the button at line 12.
18. Button loads a backup from the book_list saved with the button at line 13.
19. Button loads a backup from the loans_list saved with the button at line 14.
20. Takes the title of a book and removes it from the list.


Included Files;
this README.txt
booksset1.json; the original booksset from the assignment.
bookssetbackup.json; the backup file for the books, can be deleted and will be remade by the backup function.
FakeNameSet.csv; the originial fake nameset from the assignment.
FakeNameSetbackUp.csv; the backup file for the customers, can be deleted andw will be remade by the backup function.
loansbackup.json; the backup file for the loans, can be deleted and will be remade by the backup function.
ACTUALPLS.py; main python file.
Class Diagram.pdf