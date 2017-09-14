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
class LibraryManagement:

    def start():
        books = BookServices.Book()
        books.get_all_book()

    def add_book(self,BOOK_ID,book_name,book_author):
        books = BookServices.Book()
        books.add_book(BOOK_ID,book_name,book_author)

    def remove_book(self):
        books = BookServices.Book()
        self.get_all_book()
        book_id = input("Enter Book ID >")
        books.remove_book(book_id)

    def get_all_book(self):
        books = BookServices.Book()
        books.get_all_book()

    def get_book_map(self):
        books = BookServices.Book()
        print(books.get_book_map())

    def issue_book(self):
        books = IssueService.Issue()
        books.get_issue_map()

start = LibraryManagement()
#start.add_book(5,'Machine','sam')
#start.get_all_book()
#start.remove_book()
start.issue_book()
