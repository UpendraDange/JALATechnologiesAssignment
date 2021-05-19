"""
14. Write a program to generate NoSuchMethodException
"""


class example():
    def pyInit(self):
        self._val = 20

if __name__ == "__main__":
    try:
        obj = example()
        obj.pyINit()
    except AttributeError as ae:
        print(ae)