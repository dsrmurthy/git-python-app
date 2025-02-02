from logdemo import logger

@logger()
def square_numbers(nums):
    for i in nums:
        return  (i*i)            # so no return as we are returning generator

my_nums = square_numbers([1,2,3,4,5])
print(type(my_nums))  # class 'generator'
print(next(my_nums))  # 1 
print(next(my_nums))  
#---------------------------------------
