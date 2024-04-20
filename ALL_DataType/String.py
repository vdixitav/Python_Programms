# program 1: Reverse the given strig using slice operator

#s="Durga"
######1) 1st way :slice operator######
#s[begarn:end:step]
# s="Durga"
# op=s[::-1]
# print(op)

# s="Durga"
# op=s[::0]
# print(op)

###### 2) 2st way: REVERSE Content ####
# s="Durga"
# r=reversed(s)

# for ch in r: # return charater by charater

#   print(ch)


##### Reverse whole string####
# s="Durga"
# r=reversed(s)
# op=''.join(r)
# print(op)

##E REverse comtent of thre lst by using while loop
# s="Durga"
# op=''
# i=len(s)-1
# print(i)
# print()
# while i>=1:
#     print("i befor -",i)
#     op=op+s[i]
#     print(op)
#     i=i-1
#     print("i after -",i)

# print(op)




# s="Durga"
# op=''
# i=len(s)
# print(i)
# print()
# while i>=0:
#     print("i befor -",i)
#     op=op+s[i-1]
#     print(op)
#     i=i-1
#     print("i after -",i)

# print(op)

### write a programee to reverse a word

# s='learing python is very easy'
# l=s.split()  # it will give list of words
# print(l)

# l1=l[::-1]
# print(l1)

# op=' '.join(l1) # in empty string sace must be there
# print(op)

## write a progrm to reverse internal content of each word

# s=input('Enter any string:')
# l=s.split()
# l1=[]
# for word in l:
#     l1.append(word[::-1])

# output=' '.join(l1)
# print(l1)   

# write a progm to reverse internal content of every seconf word present in given string
# s='One two three four five six'
# l=s.split()
# print(l) 
 
# l1=[]
# i=0
# while i<len(l):
#     if i%2==0:
#         l1.append(l[i])

#     else:
#         l1.append(l[i][::-1])
#     i=i+1
#     op=' '.join(l1)
#     print(op)        

 #prgm to print char present at even index

# s='durgasoft'
# i=0
# print("cha.present at even index:")
# while i<len(s):
#     print(s[i])
#     i=i+2


## write pgrm to merge charaters of 2 strng into single string by taking ch.alternatively

# s1='ramm'
# s2='Sham'
# op=''

# i,j=0,0
# while i<len(s1) or i<len(s2):
#     op=op+s1[i]+s2[j]
#     i=i+1
#     j=j+1
# print(op)


#String creation

# str1="hello python"
# print(str1)

# mystr1='ytyty'
# mystr2=mystr1*2
# print(mystr2)

## String indexing
# str1="hello python"
# print(str1)

# m=str1[0] # 1st ch in string
# print(m)

# a=str1[len(str1)-1] #last ch of string using len()
# print(a)

# b=str1[-1] #last ch of string
# print(b)

## String Sclicing##

# c=str1[0:5] #strn sclicing fetch all ch from 0 to 5 index (4th index partyant ch fetch karel)
# print(c)

# d=str1[6:12] # retreive all ch betwn 6-12
# print(d)

# e=str1[-4:] # retreive last 4 ch of string
# print(e)

# f=str1[-6:] # print last 6 ch
# print(f)

# g=str1[:4] # 1st 4 latters
# print(g)

# h=str1[:6] # 1st 6 ch of string

# print(h)

#### Upadate and delete string ####

#str1="hello python"

# strings are immutable so cannot change

# a=str1[0:5]='eee' # it will through error
# print(a)


### delete string
# str3='maaaa'
# del str3
# print(str3)

## string concatenation

#str1="hello python"
# srt2="maaa"
# str3=str1+srt2
# print(str3)


### iteration throught string ###
# str1="hello python"
# for i in str1:
#     print(i)

# for i in enumerate(str1): # it will print with index
#     print(i)

# s2=list(enumerate(str1))

# print(s2)

## string membership

# mystr1='hello everyone'
# # print('hello' in mystr1)
# # print('me' in mystr1)

# # string partitionaing

# str5='natural lag processing and deep learning'
# l=str5.partition('and')
# print(l)


## String functions

# mystr2='  Hello everyone'
# print(mystr2)

# a=mystr2.strip()#remove white spaces from bigining and end
# print(a)

# b=mystr2.rstrip()#remove white spaces at end of string
# print(b)

# c=mystr2.lstrip()
# print(c)


# d=mystr2.lower()
# print(d)

# e=mystr2.upper()
# print(e)

# f=mystr2.replace('He','Ho')
# print(f)


# mystr4='one two three four five six one two two'
 
# a=mystr4.count('one')
# print(a)

# b=mystr4.startswith('one')
# print(b)

# c=mystr4.endswith("nine")
# print(c)

# mylist=mystr4.split()
# print(mylist)


#combining string and number using format method

# item1=40
# item2=90
# item3=80
# res="cost of item1 , item2 and item3 are {},{} and {}"
# print(res.format(item1,item2,item3))


# item1=40
# item2=90
# item3=80
# res="cost of item1 , item2 and item3 are {0},{2} and {1}"
# print(res.format(item1,item2,item3))

# str2="WELCOME EVERYONE"
# str2=str2.center(50)
# print(str2)

















