# BAD CALCULATOR PROGRAM
# this program is bad and violates KISS, DRY, Single Responsibility Principle, Separation of Concerns, and is not clean
# add sub mult all here

x = 10
y = 5
Z = 0

def a(x,y):
    # function does add but also prints and changes global variable
    global Z
    Z = x+y
    print("the answer is:",Z)
    return Z

def s(x,y):
    # subtraction but prints inside (single responsibility broken)
    global Z
    Z = x-y
    print("your number is:",Z)
    return Z

def m(x,y):
    # multiplies
    global Z
    Z = x*y
    print("result is",Z)
    return Z

#no separation of concerns
print("options: 1 add 2 sub 3 mult")
num = int(input("enter choice:"))
if num==1:
    a(2,3)
elif num==2:
    s(9,4)
elif num==3:
    m(3,3)
else:
    print("wrong")
