class Library:
    def __init__(self, book, available):
        self.book = book
        self.__available = available   

    def borrow(self):
        if self.__available:
            print(self.book, "borrowed successfully")
            self.__available = False
        else:
            print(self.book, "is not available")

    def return_book(self):
        self.__available = True
        print(self.book, "returned")

  
    def get_status(self):
        return self.__available

  
    def set_status(self, status):
        self.__available = status

    def show(self):
        print("Book:", self.book)
        print("Available:", self.__available)
        print()


b1 = Library("Python", True)
b2 = Library("C Programming", False)


b1.borrow()
b1.show()

b2.return_book()
b2.show()