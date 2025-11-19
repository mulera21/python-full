#------------------library manageent system----------------

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.borrowed = 0
    def borrow_book(self):
        if self.borrowed<self.total_copies:
            self.borrowed+=1
            print(f"Borrowed 1 copy of {self.title}")
        else:
            print(f"Sorry all copies of {self.title} are currently borrowed")

    def return_book(self):
        if self.borrowed>0:
            self.borrowed-=1
            print(f"Return 1 copy of {self.title}")
    
    def display_info(self):
        print(f"----------Book info----------")
        print(f"\tTitle: {self.title}")
        print(f"\tAuthor: {self.author}")
        print(f"\tTotal copies: {self.total_copies}")
        print(f"Borrowed Copies: {self.borrowed}")

book = Book("Alissa", "c.j more", 7 )

book.display_info()