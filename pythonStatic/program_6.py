"""
Print all the static, instance variables in main method.
"""
class school():
    Branch = "CSE"
    def __init__(self):
        self.name = "Rama"
        self.rollNo = 100


if __name__ == "__main__":
    stud = school()
    print("Name of student:",stud.name)
    print("Roll number of student:",stud.rollNo)
    print("Branch of student:",school.Branch)
