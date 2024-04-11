# try:
#     open DB connection
#     read data from db
#     close db connection= this code is called resorce deallocation /clean code

# except:
#   hanling code


# finally block ment for clean up code

 
# try:
#     risky code

# except:
#     handling code  

# finally:
#     cleanup code  

# try:
#     print("try")

# except ZeroDivisionError:
#     print("except")

# finally:
#     print("finally")            


# exception raised but handdled
# try:
#     print("try")
#     print(10/0)

# except ZeroDivisionError:
#     print("except")

# finally:
#     print("finally")                


#exception raised but not handle
try:
    print(10/0)

except ValueError:
    print('exception')

finally:
    print('finally')        
