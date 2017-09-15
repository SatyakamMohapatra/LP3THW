import BookServices
from sys import exit
from datetime import date
class Issue(object):

    """docstring for Issue."""
    def issue_book(self):
        user_id = input("Please provide user id>")
        if len(user_id) != 0:
            user_id = int(user_id)
            print(self.user_exist(user_id))
            while not(self.user_exist(user_id)):
                print("user does not exist please create a user.")
                result = input("y for create and N for exist > ")
                if result.lower() == 'y'.lower():
                    user_id = self.add_user()
                else:
                    exit(1)
            book = BookServices.Book()
            book.get_all_book()
            book_id = input("Please provide book id>")
            is_issued = book.change_stock(-1,book_id)
            if is_issued:
                self.add_issue(user_id,book_id)
        else:
            Print("enter a valid user_id:User ID can't be empty")
    def user_exist(self,user_id):
        map = self.get_issue_map()
        if user_id in map.keys():
            return True
        else:
            return False

    def add_issue(self,user_id,book_id):
        map = self.get_issue_map()
        if user_id in map.keys():
            issue_string = map[user_id]
            user_name,phone_no,current_book_id,datestr = issue_string.split(',')
            current_book_id = book_id
            d = date.today()
            datestr = d.isoformat()
            map[user_id] = f"{user_name},{phone_no},{current_book_id},{datestr}\n"
        self.set_issue_map(map)

    def add_user(self):
        user_name = input("Please provide user name >")
        phone_no = input("Please provide phone no >")
        date = None
        user_id = None
        map = self.get_issue_map()
        if len(map) >0:
            max_no = max(list(map.keys()))
            user_id = max_no+1
            map[user_id] = f"{user_name},{phone_no},0,{date}\n"
            self.set_issue_map(map)
        else:
            map[1] = f"{user_name},{phone_no},0,{date}\n"
        self.set_issue_map(map)
        return user_id

    def get_all_issues(self):
        map = self.get_issue_map()
        print("  user_id  |  user_name  |  phone_no  |  book_id  |  Issued_date  ")
        print('_'*70)
        for user_id,issue_string in map.items():
            user_name,phone_no,book_id,Issued_date = issue_string.split(',')
            print(f"     {user_id}     |     {user_name}     |     {phone_no}     |     {book_id}     |     {Issued_date}     ")
        print('_'*70)

    def get_issue_map(self):
        self.map = {}
        with open("issueMaster.txt",'r') as issue_master:
            issue_array = issue_master.readlines()
        if len(issue_array) > 0:
            for issue in issue_array:
                user_id,name,mobile_no,book_id,Issued_date = issue.split(',')
                self.map[int(user_id)] = f"{name},{mobile_no},{book_id},{Issued_date}"
        return self.map

    def set_issue_map(self,map):
        with open("issueMaster.txt",'w') as issue_master:
            for user_id,issue_string in map.items():
                user_name,phone_no,book_id,Issued_date = issue_string.split(',')
                issue_master.write(f"{user_id},{user_name},{phone_no},{book_id},{Issued_date}")
