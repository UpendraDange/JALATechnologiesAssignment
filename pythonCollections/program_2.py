"""
2. Create a HashMap with at least 10 key value pairs of the Student ID and Name
    Insert a Key value mapping into the map
    Fetch the value of a Key
    Create a clone/copy of HashMap
    Check if the given Key is in the Map
    Check if the value is in the Map
    Check if the map is empty
    Print the size of the Map to the console
    Print all the Keys of the map to the console
    Print all the Keys of the map to the console
    Remove a specific Key-value pair
    Copy all the elements of the Map to another Map

"""

pyDict = {1:"upendra", 2:"mayur", 3:"sagar",
          4:"vaibhav", 5:"vishal", 6:"dikshant",
          7:"subhash", 8:"akshay", 9:"ramesh",
          10:"suresh"}

pyDict[11] = "rama"     #Insert a Key value mapping into the map

print(pyDict.get(6))       #Fetch the value of a Key

pyDict2 = pyDict.copy()     #Create a clone/copy of HashMap
print(pyDict2)

print(4 in pyDict)          #Check if the given Key is in the Map

for i in pyDict:            #Check if the value is in the Map
    count = 0
    if pyDict.get(i) == "suresh":
        print("value present in dictionary")
        count = 1
if count == 0:
    print("value not present in dictionary")


print(len(pyDict) == 0)         #Check if the map is empty

print(len(pyDict))      #Print the size of the Map to the console

print(pyDict.keys())        #Print all the Keys of the map to the console

pyDict.pop(6)       #Remove a specific Key-value pair





