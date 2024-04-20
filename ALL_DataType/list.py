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

# n=[1,2,3,4,5]
# print(n.pop())
# print(n)


# a='hello'
# b=list((X.upper(),len(X)) for X in a)
# print(b)

# lst=[3,4,6,1,2]
# lst[1:2]=[7,8]
# print(lst)

# a=[1,2,3,4]
# b=[sum(a[0:x+1])for x in range(0,len(a))]
# print(b)

# import copy
# a=[10,23,56,[78]]
# b=copy.deepcopy(a)
# a[3][0]=95
# a[1]=34
# print(b)

# print(list(zip(1,2,3),('a'),('XXX','YYY')))
# print(list(zip(2,4),('b','c'),('yy','xx')))

# a=[[]]*3
# a[1].append(7)
# print(a)

# a=[10,23,56,[78]]
# b=list(a)
# a[3][0]=95
# a[1]=34
# print(b)

# a=165
# b=sum(list(map(int,str(a))))
# print(b)

# x=[[1],[2]]
# print(''.join(list(map(str,x))))

# lst=[[1,2],[3,4]]
# print(sum(lst[]))

# def unpack(a,b,c,d):
#       print(a+d)

# x=[1,2,3,4]
# unpack(*x)    

# a=[14,52,7]
# b=a.copy()
# b is a
# print(b)

# a=list((45,)*4)
# print((45)*4)
# print(a)

# a=[1,2,3]
# b=a.append(4)
# print(a)
# print(b)

# a=[13,56,17]
# a.append([87])
# a.extend([45,67])
# print(a)

# word1='Apple'
# word2='Apple'
# list1=[1,2,3]
# list2=[1,2,3]
# print(word1 is word2)
# print(list1 is list2)



# list slicing

# mylist=['one','two','three','four','five','six','seven','eight']

# a=mylist[0:3]
# print(a)

# b=mylist[2:5]
# print(b)

# c=mylist[0:3]
# print(c)

# d=mylist[:2]
# print(d)

# e=mylist[-3:]
# print(e)

# f=mylist[:-3]
# print(f)

# add ,remove , change items

#print(mylist)

# a= mylist.append('six')
# print(a)

# mylist[0]=90
# print(mylist)

# reverse and sort lsi

#list1=['one','two','three','four','five','six','seven','eight']
# list1.reverse()
# print(list1)

# list1=list1[::-1]
# print(list1)

# loop through a list

#print(list1)
list1=['one','two','three','four','five','six','seven','eight']
# for i in list1:
#   print(i)

# for i in enumerate(list1):
#     print(i) 

# m=list1.count('nine') 
# print(m)

L2=[1,2,3,4,5,0]
print(all(L2))

print(any(L2))




