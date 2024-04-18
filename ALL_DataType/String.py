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

s='learing python is very easy'
l=s.split()  # it will give list of words
print(l)

l1=l[::-1]
print(l1)

op=' '.join(l1) # in empty string sace must be there
print(op)




