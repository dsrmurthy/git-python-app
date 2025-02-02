Notes on python:
--------------
primitive types: int,float,double ,str,boolean.....   (dynamic)
sal=5000.0
ref. types

1. list : collection of items of hetrogeneous  []
       data=[10,true,'murthy']
       data.append('techmojo')
       print(data)
2. dict :  { }  key:value : JSON
     emps=[
        {eno:101,name:'lalitha',phones:[424324,432424]},
        {eno:101,name:'lalitha',phones:[424324,432424]}
        {eno:101,name:'lalitha',phones:[424324,432424]}
     ]

3. tuple : ( ) : not editable (readonly)

    data=(
        { 'pid':1,'pname':'mouse','discount':100}
    )

    info=(101,'murthy',[343,4343])

    data= [
        {
        pid: 101,
        pname:'mouse',
        invoice :{
            invno:1,
            cname:'murthy'
            contacts: (4i3429042,43242424)
        }
    },
    {
        pid: 102,
        pname:'mouse',
        invoice :{
            invno:2,
            cname:'murthy'
            contacts: (4i3429042,43242424)
        }
    }
    ]

    list : map, sort , filter ,reduce.....

================================================================
To deactivate : cd env/scripts
     deactivate

To create env:
C:> md pythonnewapp
c:/> cd pythonnewapp
c:\pythonnewapp> python -m venv myenv
c:\pythonnewapp> cd myenv/scripts
    ...>activate
    ...
    deactivate

    iterator vs generator vs decorator  (custom )
    Data management (csv, json, binary (pickle))
    DB managment (Sqllite3..........)- ORM

    OOP:  
    ================
    custom iterator:
    1. create class with name Paginator
    2. constructor to receive initial paramers for size of page 
    3. override __iter__() to tell iterator class 
    4. override __next__() to fetch data from api/db as per size 

    5. test it 

    Generator:
    Generator uses iterator
    To improve performance for big data (memory)

    data=[1,2,3,4,5]
    def getdata(mylist):
    for item in data:
        yield item.item
    
   d=getdata()
   print(d.__next__())
   print(d.__next__())
   print(d.__next__())
   =====================================================
   Decorator:
   Attaching additional responsibilities to existing function/method/class for diffrent behaviour.  Extensibility

   Cross cutting concert:
   PAL :  client view
   BAL : BL 
   DAL : DB access (sqlite3)
   IAL : security , caching , logging, profiling, tracing..... (Decorators)

AOP 

#HOF 
def sayHello(name):
    return f"hello {name} "

def appreciate(name):
   return f" yo! {name}, you are great

#broker
def broker(func,name):
    console.log(f' some one called {func.__name__} ')
    console.log('valid user')
    func()

print(broker(sayHello,'murthy'))
print(broker(appreceate,'murthy'))

import logging

severity levels

DEBUG
INFO
WARNING
ERROR 
CRITICAL 
======================
file system:
POSIX program
w,w+,a,r,r+,bwbbr.......


fp=open('sales.csv','r')
    ................................
fp.close()

IO: file, db,socket,process

context manager  : with
with open('sales.csv','r')  as fp:
    ..........

reader and writer  reads lin eby line
dictReader and dictWriter : 


Working with JSON data:

REST API:
Packages:  http calls 
requests lib
urllib3
httplib2

json  = json.loads()
json.load()
json.dump()
json.dumps()


Serialization and deser:
file,database,socket
memory,file, db
---------------------------------
Binary serialization: bits and bytes (0,1's) 
     security - the file is not readable.
     size of the file is reduced by 20 - 30%
     transferring the data on network system gives performance
     easy to use

     

import pickle

Pickling is a process of serializing python objects(list,dict,tuple,custom type) by coverting into bits and bytes (0,1)
flattening, marshalling,seralizing......

x : only python objects can be pickled and other languages can not read pickled data

pickle.pickleException    unpickleException
