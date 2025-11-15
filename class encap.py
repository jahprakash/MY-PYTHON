class encap:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

s = encap("jahnavi")
print(s.get_name())

s.set_name("chandan")
print(s.get_name())
