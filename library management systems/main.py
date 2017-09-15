"""
Library Management System
Flow:->
1. Create a Libery DB >
    1. BOOK_ID,BOOK_NAME,AUTHOR,LAST_UPDATED_BY,LAST_UPDATED_DATE
    2. BOOK_ID,ISSUED_DATE,ISSUED_BY_ID,ISSUED_TIMES,,LAST_UPDATED_BY,LAST_UPDATED_DATE
    3. BOOK_ID,TOTAL_STOCK,CURRENT_STOCK
    4. BOOK_TYPE,BOOK_ID
    5. BOOK_ID,BOOK_LOCATION
    6. ISSUED_BY_ID,NAME,ADDRESS,CONTACT_NO,GOVT_ID,TOTAL_BOOKS_ISSUED
2. Create A master interface in python
3. search for a BOOK
    1. if found issue the book or go to master page
    2. Return a book
    3. Email the Issuer of the book to return
4. Find Current in stock
5. ADD A new book to the repo or increase the quentity
ADVANCE
6. BY BOOK_ID search web to get name and author name and book type
7. Assortment Planning
"""
import BookServices
import IssueService
from sys import exit

class LibraryManagement:
    def __init__(self):
        self.serv_dic = {
            1:"add_book",
            2:"remove_book",
            3:"get_all_book",
            4:"get_all_issues",
            5:"issue_book",
            0:"exit"
        }
        input("Welcome to LM Services > \"Enter to continue!\"")

    def start(self):
        print(f"""
        Please seletct from the options:
        {'_'*70}
        1 for add a new book
        2 for remove a book from stock
        3 for get all books avalable in Libery
        4 for details of all users
        5 for issuing a book
        0 for exit
        """)
        option = int(input("Provide you option > "))
        self.run(option)

    def run(self,option):
        service_map = self.serv_dic
        while option != 0:
            if option == 1:
                self.add_book()
                self.start()
            elif option == 2:
                self.remove_book()
                self.start()
            elif option == 3:
                self.get_all_book()
                self.start()
            elif option == 4:
                self.get_all_issues()
                self.start()
            elif option == 5:
                self.issue_book()
                self.start()
            else:
                print("enter a valid option")
                self.start()
        exit(1)
    def add_book(self):
        books = BookServices.Book()
        books.add_book()

    def remove_book(self):
        books = BookServices.Book()
        self.get_all_book()
        book_id = input("Enter Book ID >")
        books.remove_book(book_id)

    def get_all_book(self):
        books = BookServices.Book()
        books.get_all_book()

    def issue_book(self):
        books = IssueService.Issue()
        books.issue_book()

    def get_all_issues(self):
        books = IssueService.Issue()
        books.get_all_issues()


start = LibraryManagement()
start.start()
