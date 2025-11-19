#------------------library manageent system----------------

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.__total_copies = total_copies
        self.__borrowed = 0
    def borrow_book(self):
        if self.__borrowed<self.__total_copies:
            self.__borrowed+=1
            print(f"Borrowed 1 copy of {self.title}")
        else:
            print(f"Sorry all copies of {self.title} are currently borrowed")

    def return_book(self):
        if self.__borrowed>0:
            self.__borrowed-=1
            print(f"Return 1 copy of {self.title}")
        else:
            print(f"No copies of {self.__borrowed}")
    def get_availability(self):
        return self.__total_copies - self.__borrowed
    
    def display_info(self):
        print(f"----------Book info----------")
        print(f"\tTitle: {self.title}")
        print(f"\tAuthor: {self.author}")
        print(f"\tTotal copies: {self.__total_copies}")
        print(f"Borrowed Copies: {self.__borrowed}")
        print(f"\t Available copies: {self.get_availability()}")
        print(f"----------------------------------")

book = Book("Alissa", "c.j more", 7 )

book.display_info()
book.borrow_book()
book.__total_copies = 10
book.__borrowed = 15
book.borrow_book()
book.borrow_book()
book.borrow_book()
book.return_book()
book.display_info()