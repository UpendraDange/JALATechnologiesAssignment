"""
Write a method for increment and decrement operator(++, --)

ans:  Increment and Decrement operators are not allowed in it.
      Instead  of Increment and Decrement operators, for Increment the count
      we can use i+=1 or i-=1
"""

class IncDec():
    def inc_method(self,count):
        for i in range(5):
            count+=1
        return count

    def dec_method(self, count):
        for i in range(5):
            count -= 1
        return count

obj=IncDec()
print("After Incrementing count:",obj.inc_method(4))
print("After Decrementing count:",obj.dec_method(8))