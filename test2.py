from tkinter import *
book_list = []
def add_book_to_library(author, country, image, language, link, pages, title, year):
    book_list.append({"author": author, "country": country, "imageLink": image, "language": language, "link": link, "pages": pages, "title": title, "year": year})



add_book_to_library("TstAuthor", "TestCountry",  "images/TestImage", "TestLanguage",  "Testlink\n",  1,  "No",  1836)


print(book_list)