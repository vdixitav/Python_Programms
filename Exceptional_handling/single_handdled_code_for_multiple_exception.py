try:
    x=int(input("enter 1st number:"))
    y=int(input("enter 2nd number"))
    print("result:",x/y)

except(ZeroDivisionError ,ValueError) as msg:
    print('Exception name :',msg.__class__.__name__)
    print("plz provide correct value ")
  