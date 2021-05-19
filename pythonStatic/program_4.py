"""
Call instance methods in static methods.
"""

class Hello():
    def Instance_method(self):
        print("I am in Instance method")
    @staticmethod
    def static_method(obj):
        print("I am in static method")
        obj.Instance_method()

obj=Hello()
Hello.static_method(obj)