"""
3. Create a HashSet with at least 10 elements of type String
    Write program covering all the operations of HashSet
"""

pySet1 = {"Sachin", "Dhoni", "Virat", "Rohit",
          "Dhavan", "Shubhman", "Pujara", "Pant",
          "Jadeja", "Shami"}

pySet2 = {"mayur", "sagar", "Virat",
          "Rohit", "vishal", "dikshant",
          "Pant",}

pySet1.add("Kumar")     #add element in set

pySet3 = pySet1.copy()  #copy all element of one set to another set
print(pySet3)

pySet3.clear()   #remove all element from set

print(pySet1.difference(pySet2))

pySet1.difference_update(pySet2)

pySet1.discard("Dhavan")

pySet1.add('Virat')
pySet1.add('Rohit')

print(pySet1.intersection(pySet2))

pySet1.intersection_update(pySet2)

print(pySet1.isdisjoint(pySet2))

print(pySet1.issubset(pySet2))

print(pySet1.issuperset(pySet2))

print(pySet2.pop())

pySet2.remove("mayur")

print(pySet1.symmetric_difference(pySet2))

pySet2.symmetric_difference_update(pySet1)

pySet3 = {"Pant", "Sachin"}
pySet1.update(pySet3)

print(pySet1.union(pySet2))


print(pySet1)
print(pySet2)
