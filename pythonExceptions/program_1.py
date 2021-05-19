"""
Write a program to generate Arithmetic Exception without exception handling


"""

def sample():
    val1 = int(input("Enter first number:"))
    val2 = int(input("Enter second number:"))

    if val2 == 0 :
        print("You should not divide a number by zero. ")
    else :
        print("Division is :",val1/val2)

if __name__ == "__main__":
    sample()