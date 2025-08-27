# add 2 list using map and lambda
list1=[1,2,3]
list2=[4,5,6]
addition=map(lambda x,y:x+y,list1,list2)
print(f"the addition of two list is {list(addition)}")

# square of list using map in list
list5=[2,6,36,6,7]
def square(n):
    return n*n
result=list(map(square,list5))
print(f"the result of square is {result}")