import sqlite3
# Data Access Layer functions to perfrom crud on db
#  Code first approach
#  DB first approach
from employee import Employee

def connectDB():
    global conn
    conn=sqlite3.connect("employes.db")
    global  cursor
    cursor=conn.cursor()
    print("Connected to Database")
#----------------------------------------

def createTable():
    try:
        cmd="CREATE TABLE  emps(fname text, lname text, pay integer)"
        cursor.execute(cmd)
        print("emps table is created")
    except Exception as ex:
        print("Can not create table",ex)

def insertEmp(emp):
    try:
        cmd= "INSERT INTO emps (fname,lname,pay) VALUES(?,?,?)"
        values=(emp.fname,emp.lname,emp.pay)
        cursor.execute(cmd,values)
        cursor.execute("commit")
        print("One employee added to database table")
    except Exception as ex:
        print("Error in inserting")
#----------------------------   

def readEmps():
    cursor.execute("SELECT * FROM emps")
    return cursor.fetchall()
#=============================
def deleteEmp(emp):
    try:
        cursor.execute("DELETE FROM emps WHERE :lname= last" ,{'last':emp.lname})
        cursor.execute('commit')
    except Exception as ex:
        print(ex)

# Test code
print("working with sqlite3 database")
connectDB()
#createTable()
#emp1= Employee('Murthy','Sriram',50000)
#emp2=Employee('Kiran','Kumar',40000)
#insertEmp(emp1)
#insertEmp(emp2)
data=readEmps()
print(data)

print("After deleting ")
emp1= Employee('Murthy','Sriram',50000)
deleteEmp(emp1)

data=readEmps()
print(data)

cursor.close()
conn.close()  # memory leak

