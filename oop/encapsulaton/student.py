#============encapsulation in Python============#

class Student:
    def __init__(self, name, age, grade):
        self.__name = name          # private attribute
        self.__age = age            # private attribute
        self.__grade = grade        # private attribute

   