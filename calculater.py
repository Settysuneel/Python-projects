
#this is calculator
print("press 1 addition")
print("press 2 subtraction")
print("press 3 multiplication")
print("press 4 Division")
print("press 5 power")
print("press 6 module division")
c=int(input("select the above operation"))
a=int(input("enter the number"))
b=int(input("enter the number"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
elif c==5:
    print(a**b)
elif c==6:
    print(a//b)
else:
    print('unavailable') 
    
