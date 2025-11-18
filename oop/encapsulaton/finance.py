#-------------------encapsulation------------------

class Finance:
    def __init__(self):
        self.revenue = 100000
        self.number_of_sales = 114

f1 = Finance()

class HR:
    def __init__(self):
        self.number_of_emp= 32
        print(f1.revenue)

h1 =HR()