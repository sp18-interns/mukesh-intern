try:
   f = open('testfile','r')
   f.write("write a text line")
except:
    print('All other exceptions!')
finally:
    print("I always run")