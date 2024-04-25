try:
    print(100/0)

except:
    print(sys.exc_Info()[1],'excepation occured')

else:
    print('no excption occured')

finally:
    print('run this block always')            