"""
3. Write a method which throws exception, Call that method in main class without try block

"""

x=int(input("Enter Any Number: "))
if x<=10:
    raise ValueError('x should not be less than 10!')
else:
    print("Great Value")
