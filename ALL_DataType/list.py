# empty list creation

# list=[]
# print(list)
# print(type(list))

# element present
#list=[10,20,30,40]

#with dynamic i/p

# list=eval(input('enter list:'))
# print(list)
# print(type(list))

#with list()function
# l=list(range(0,10,2))
# print(l)
# print(type(l))

# s='durga'
# l=list(s)
# print(l)


########split()function######

# s='learning python is very very easy'
# l=s.split()
# print(l)
# print(type(l))


####Accessing element of the list ####

# 1) using index
# list1=[10,20,30,40,50]
# print(list1[0])
# print(list1[4])
# print(list1[9])

# 2) using slice operation

#syntx:
# list2=list1[start:stop;steps]

#n=[1,2,3,4,5,6,7,8,9,10]
#print(n[2:7:2])
#print(n[4::2])
#print(n[3:7])
#print(n[8:2:-9])
#print(n[4:100])

## mutability##

# n=[10,20,30,40]
# print(n)
# n[2]=90
# print(n)

### traversing the element of list: sequential access of each element

# 1) using while loop
# n=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(n):
#     print(n[i])
#     i=i+1

# 2) using for loop
# n=[1,2,3,4,5,6,7,8,9,10]
# for s1 in n:
#     print(s1)

# 3) to display only even number

# n=[1,2,3,4,5,6,7,8,9,10]
# for s1 in n:
#     if s1%2 ==0:
#         print(s1)


# 4) to display only odd number

# n=[1,2,3,4,5,6,7,8,9,10]
# for s1 in n:
#     if s1%2 !=0:
#         print(s1)

# 5) to disply elements by indexwise

# l=['A','B','C']
# x=len(l)

# for i in range(x):
#     print(l[i],"Is availble for positive index:",i,"and at negative index:",i-x)


# list functions

# 1) len()  --> return the number of elements present in list

# n=[10,20,30]
# print(len(n))

# 2) count():return no.of occurance of specific items in list

# n=[1,2,3,4,5,6,7,8,8,8]
# print(n.count(8))

# 3) index(): will return 1st occurance of specific item

# n=[1,2,3,4,5,6,7,8,8,8]
# print(n.index(8))

## manipulating elements of list

# 1) append(): to add items at the end of the list

# list=[]
# list.append("A")
# print(list)


# To add all elements in list upto 100 divisible by 10

# list=[]
# for i in range(101):
#     if i%10==0:
#         list.append(i)

# print(list)      

# 2) insert():insert item at specified index position

# n=[1,2,3,4,5]
# n.insert(0,10)  # (index,value)

# print(n)

# 3) extend(): add all items of one list to other list

# order1=['test1','Test2','test3']
# or2=['tim']
# order1.extend(or2)
# print(order1)

# 4) pop(): remove and retuen last elemet

n=[1,2,3,4,5]
print(n.pop())
print(n)

