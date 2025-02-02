#iterator design pattern 
data=[10,20,30,40]
#print(data[2])
#for i in data:
#   print(i) #iterator
''' 
d=iter(data)
print(type(d))
print(d.__next__())
print(d.__next__())
print(next(d))
print(next(d))
print(next(d))
'''
#pandas.head(100)
#pandas.tail(10)
# custom iterator
class Head:
    def __init__(self,size=5):
        self.num=1
    
    def __iter__(self):
        return self

    def __next__(self):
        # write DB , REST api calls or load local csv data
        if self.num<=5:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration
#--------------------------------------------------
# test code
values=Head(100)
for i in values:
    print(i)


https://jsfiddle.net/mqap52do/

