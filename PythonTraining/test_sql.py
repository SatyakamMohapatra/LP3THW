import sqlite3
from test import Employee

conn = sqlite3.connect('empolyee.db')
c = conn.cursor()

def create_employee():
    with conn:
        c.execute("""
                    CREATE TABLE Employee (
                                        first text,
                                        last text,
                                        pay integer)
                    """)
def add_employee(emp):
    """
    add_employee to the DB
    """
    with conn:
        c.execute("INSERT INTO Employee VALUES (?,?,?)",
                                               (emp.first,emp.last,emp.pay))

def get_all_employee():
    """
    get_employee to the DB
    """
    emp_list = []
    with conn:
        c.execute("SELECT * from Employee")
        emp_list= c.fetchall()
    return emp_list

def delete_employee(first):
    """
    get_employee to the DB
    """
    with conn:
        c.execute("DELETE From Employee where first = ?",(first,) )
