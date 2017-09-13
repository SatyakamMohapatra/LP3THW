class Book(object):
    """docstring for BookServices."""
    def __init__(self):
        pass

    def add_book(self,book_name,book_author):
        with open("bookMaster.txt",'r+') as book_master:
            if book_name and book_author:
                book_array = book_master.readlines()
                #print(book_array)
                if len(book_array) > 0:
                    #print("line_list")
                    line_list = book_array[len(book_array)-1].split(',')
                    #print(line_list)
                    if len(line_list) ==3:
                        previous_id,previous_name,previous_author = line_list
                        current_id = int(previous_id)+1
                        #print("current_id")
                        book_master.write(f"{current_id},{book_name},{book_author}\n")
                else:
                    print("True")
                    current_id = 1
                    book_master.write(f"{current_id},{book_name},{book_author}\n")

    def get_all_book(self):
        with open("bookMaster.txt",'r+') as book_master:
            if book_master:
                book_array = book_master.readlines()
            if len(book_array) > 0:
                print(f"BookID   |  book_name  |  book_author  ")
                print("-"*50)
                for book in book_array:
                    line_list = book.split(',')
                    current_id,book_name,book_author = line_list
                    print(f"BookID = {current_id} | book_name = {book_name} | book_author = {book_author}")
                print("-"*50)
