#------------------library manageent system----------------

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.borrowed = 0
    
    def display_info(self):
        