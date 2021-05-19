"""
Print gender (Male/Female) program according to given M/F
using switch
"""
def demo(arg):
    switcher = {
        'M': "Male",
        'F': "Female",
    }
    return switcher.get(arg,"Please enter valid Input")

if __name__ == "__main__" :
    gen = input("Enter a gender as M or F:")
    print(demo(gen))