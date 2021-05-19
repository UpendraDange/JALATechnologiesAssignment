"""
    Define the local and Global variable with the same name and
    print both variables and understand the scope of the variable

    ans :
    local variable :The variables defined within the function has a local scope and hence they are called local
                    variables. Local scope means they can be accessed within the function only
"""

total = 0   #Global Variable
def sum(arg1,arg2):
    total=arg1+arg2     #local variable
    print("Inside the function local total :",total)
    return total
sum(10,40)
print("Outside the function global total:",total)

"""
global keyword
    It is used to declare that a variable inside the function is global (outside the function).
    If we need to read the value of a global variable, it is not necessary to define it as global. If we need to
    modify the value of a global variable inside a function, then we must declare it with global.

"""

x=100
def MyFun():
    global x
    x=5         #global variable x has assign 5
    y=20
    print(x+y)

def MyFun1():
    y=10
    print(x+y)

MyFun()
MyFun1()