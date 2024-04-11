# x=int(input('enter first number'))
# y=int(input('enter 2nd number'))
# print('the result;',x/y)

# zeroDivisionError
#valueError

# f=open('xyzxyz.txt')
# print(f.read)

#FileNotFoundError

#What is excepton?= unwanted or unexpected event in bewtween normal flow

#Purpose of exceptional handling?=gressfull termination of programme



#Default Exceptional Handling

# print("hello")
# print(10/0)
# print('HI ')


#How to print excepton info to consol

try:
    print(10/0)

except ZeroDivisionError as msg:
    print('Exception Type :',type(msg))  
    print('The tyep of exception :',msg.__class__ )  