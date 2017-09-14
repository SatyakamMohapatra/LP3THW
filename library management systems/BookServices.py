class Book(object):
    """docstring for BookServices."""
    def __init__(self):
        pass

    def add_book(self,BOOK_ID,book_name,book_author):
        map = self.get_book_map()
        if int(BOOK_ID) in map:
            value = map.get(BOOK_ID)
            book_name,book_author,stock = value.split(',')
            stock = int(stock)+1
            map[BOOK_ID] = f"{book_name},{book_author},{stock}\n"
        else:
            map[BOOK_ID] = f"{book_name},{book_author},0\n"
        self.set_book_map(map)

    def get_book_map(self):
        self.map = {}
        with open("bookMaster.txt",'r') as book_master:
            book_array = book_master.readlines()
            if len(book_array) > 0:
                for book in book_array:
                    current_id,book_name,book_author,stock = book.split(',')
                    self.map[int(current_id)] = f"{book_name},{book_author},{stock}"
        return self.map

    def set_book_map(self,map):
        with open("bookMaster.txt",'w') as book_master:
            for key,value in map.items():
                book_name,book_author,stock = value.split(',')
                book_master.write(f"{key},{book_name},{book_author},{stock}")

    def get_all_book(self):
        map = self.get_book_map()
        print("  BOOK_ID  |  book_name  |  book_author  |  stock  ")
        print('_'*50)
        for key,value in map.items():
            book_name,book_author,stock = value.split(',')
            print(f"     {key}     |     {book_name}     |     {book_author}     |     {stock}     ")
        print('_'*50)

    def remove_book(self,book_id):
        map = self.get_book_map()
        book_id = int(book_id)
        if book_id in map:
            del map[int(book_id)]
            self.set_book_map(map)
        else:
            print(f"Book with book_id: {book_id} not present")
