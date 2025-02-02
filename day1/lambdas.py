

#single line functions are lambda functions
add5=lambda x : x+5

print(type(add5))
print(add5(100))

sm=lambda x=10:True if x.startswith('M') else False
print(sm('murthy'))

alist=['learn','python','step','by','step']
output=list(map(lambda x:x.upper(),alist))
print(type(output))
print(output)
#-------------------------------------------------------------------
#[], (), [{],{}}]
#filter
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# def is_A_student(score):
#     return score > 75
checker=lambda x: x>75
over_75 = list(filter(checker, scores))
print(over_75)


#sort
list1=[("eggs",5.25),("honey",9.5),('carrots',1.4)]
list1.sort(key =lambda x:x[1],reverse=True)
#True=1  False=0
print(list1)




