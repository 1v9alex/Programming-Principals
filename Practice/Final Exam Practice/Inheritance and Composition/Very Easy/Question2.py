class Author:
    def __init__(self,name):
        self.name = name
    
    def display_info(self):
        print(f"Author: {self.name}")



class Book:
    def __init__(self,title,author: Author):
        self.title = title
        self.author = author
        
    def display_name(self):
        print(f"Book: {self.title}")
        self.author.display_info()
        

author1 = Author("Alex")
book1 = Book("Alex is the best", author1)

book1.display_name()