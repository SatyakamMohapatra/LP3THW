import BookServices
class Issue(object):
    """docstring for Issue."""
            def issue_book(self):
                with open("issueMaster.txt",'') as file:

            def get_issue_map(self):
                self.map = {}
                with open("issueMaster.txt",'r') as issue_master:
                    issue_array = issue_master.readlines()
                    if len(issue_array) > 0:
                        for issue in issue_array:
                            user_id,name,mobile_no,book_id = issue.split(',')
                            self.map[int(user_id)] = f"{name},{mobile_no},{book_id}"
                return self.map

            def set_issue_map(self,map):
                with open("issueMaster.txt",'w') as issue_master:
                    for key,value in map.items():
                        book_name,book_author,stock = value.split(',')
                        book_master.write(f"{key},{book_name},{book_author},{stock}")
