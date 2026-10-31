class book:
    def __init__(self,title,author,is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True
        print(self.title,"-",self.author,"is borrowed")

    def return_book(self):
        self.is_borrowed = False
        print(self.title,"-",self.author,"is returned")

b1 = book("the little wingman","josh henry")
b2 = book("the red hen","joseph jane")

books = [b1,b2]

for book in books:
    book.borrow()
    book.return_book()