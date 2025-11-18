#-------------------encapsulation------------------

class Finance:
    def __init__(self):
        self.__revenue = 100000 #private data
        self.number_of_sales = 114

    def get_revenue(self):
        return self.__revenue

f1 = Finance()

class HR:
    def __init__(self):
        self.number_of_emp= 32
        print(f1.get_revenue())

h1 =HR()