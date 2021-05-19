"""
1. Create an ArrayList of type String with 10 string elements. Add 10 string elements to
    ArrayList and perform the below operations
    Add an element to the ArrayList
    Iterate through the ArrayList by using Iterator object
    Add an element at a specific index
    Remove an element from the ArrayList, Remove at an index
    Update the element at a specific index
    Check the element is present at a particular index
    Get an element at a particular index
    Find out the size of the ArrayList
    Check the given element is present in the ArrayList
    Remove all elements of the ArrayList
"""

pyList = ["Sachin", "Dhoni", "Virat", "Rohit",
          "Dhavan", "Shubhman", "Pujara", "Pant",
          "Jadeja", "Shami"]

pyList.append("Bumrah")         #Add element in  list

pyIter = iter(pyList)           #Iterate through the ArrayList by using Iterator object
for i in range(len(pyList)):
    print(next(pyIter))

pyList.insert(2, "Sehwag")      #Add an element at a specific index

pyList.pop(4)
pyList[4] = "Rohit"         #update

print(pyList[6] == "Sachin")  #Check element of perticular index

print(pyList[6])            #Get an element at a particular index


print(len(pyList))  #Find out the size of the ArrayList

print("Shami" in pyList)        #Check the given element is present in the ArrayList

pyList.clear()          #Remove all elements of the ArrayList

