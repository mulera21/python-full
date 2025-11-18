#------------encapsulation----------------

class School:
    def __init__(self):
        self.department = 56
        self.__section = 122

    def get_section(self):
        return self.__section
    
s1 = School()

class Dean:
    def __init__(self):
        self.student = 134
        print(f"we have {s1.get_section()}")

d1 = Dean()