''' Custom module : app.py '''
import os,sys
def converter(mylist):
    result=[]
    for item in mylist:
        citem=item.upper()
        result.append(citem)
    return result

name="murthy"  # global variable
add5= lambda x:x+5

def  greet(ename):
    print(add5)
    os.system('cls')
    data=[10,20,'Murthy']   # private variable
    print(type(data))
    print(data)
    emps=[
        {'eno' : 101,'ename': 'Laxme'},
         {'eno' : 102,'ename': 'Murthy'}
    ]
    print(type(emps))
    print(emps)
    first,second=(100,200)
    print(first)

    
   


if  __name__=='__main__':
    greet("kiran")

    sys.exit()
    
    
