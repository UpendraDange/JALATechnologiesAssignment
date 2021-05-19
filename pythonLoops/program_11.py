"""
Program to check whether a number is EVEN or ODD using switch

"""
def demo(arg):
    switcher = {
        0: "EVEN",
        1: "ODD",
    }
    return switcher.get(arg)

if __name__ == "__main__" :
    num = int(input("Enter a number:"))
    print("Number is:",demo(num%2))