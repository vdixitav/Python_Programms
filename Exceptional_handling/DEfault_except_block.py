try:
    x=int(input('enter 1st number:'))
    y=int(input('enter 2nd number'))

    print('reslt:',x/y)

  

except ZeroDivisionError:
     
    print('Divide by zero')

# except:
#     print("DEfault exception block")     