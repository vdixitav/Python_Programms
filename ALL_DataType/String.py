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








