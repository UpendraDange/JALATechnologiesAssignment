"""
1. Write a class with a default constructor, one argument constructor and two argument
constructors. Instantiate the class to call all the constructors of that class from a main
class

NOte : Python doesn’t support multiple constructors,
        yet there are some ways using which the multiple constructors can be achieved.
         If multiple __init__ methods are written for the same class,
         then the latest one overwrites all the previous constructors,
"""


class sample:

    def __init__(self, *args):
        self.args = args
        if len(self.args) > 1:
            self.ans = 0
            for i in self.args:
                self.ans+=i
            print("addition of list:",self.ans)

        elif isinstance(args[0], int):
            self.ans = args[0] ** 3
            print("cub of value:",self.ans)

if __name__ == "__main__":
    d1 = sample(10, 20)
    d2 = sample(8)