"""
Write a program to find Armstrong number or not.
"""
num=input("Enter a number:")
lenght=len(num)
pynum = int(num)
temp = pynum
res=0
while temp > 0:
    rem = temp%10
    rem = rem**lenght
    temp = temp//10
    res+=rem
if res == pynum:
    print("Number is Armstrong number")
else:
    print("Number is not Armstrong number")