# zip element of two list
list1=[3,2,9,6,"h","i","m"]
list2=[1,4,5,76,"w","k","hdgdjeh"]
list3=list(zip(list1,list2))
print(list3)

#print elements on by one but elements of list 2 will be reverse order
for x,y in zip(list1,list2[::-1]):
    print(x,y)

# zip into dictionary
dict={i:j for i,j in zip(list1,list2)} 
print(dict)