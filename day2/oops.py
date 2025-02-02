#oops module
class Employee(object):
    #constructor
    def __init__(self,empno,ename,salary):
        self.eno=empno   #instance variables/properties
        self.name=ename
        self.pay=salary
        self.__bonus=10000  #private instance property

    def showDetails(self): #instance method
        print('Em.pno  ',self.eno)
        print('Emp name  ',self.name)
        print('Salary  ',self.pay)
        print('total amt',self.pay+self.__bonus)

    @staticmethod
    def getCompany():
        return "Techmojo"
#---------------------------------
if __name__=='__main__':
    e1=Employee(101,'Murthy',50000)
    e1.showDetails()
    e2=Employee(102,'Kiran',30000)
    e2.showDetails()  
    print(e1.__bonus)