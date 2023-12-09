class Book:
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def displayinfoBook(self):
        print(f"the title is {self.title}, the author is {self.author}, the publication year is {self.publication_year}")


class FictionBook(Book):
    def __init__(self,genres):
        self.genres = []
    
    def addGenre(self,genre):
        self.genres.append(genre)
        return self.genres
    
    def whatGenres(self):
        print(f"This books genre(s) are {self.genres}")
        
class NonFictionBook(Book):
    def __init__(self,subject,title,author,publication_year):
        super().__init__(title,author,publication_year)
        self.subject = subject
    
    def whatSubject(self):
        print(f"This book Subject is {self.subject}")


newB = Book("100 reasns why alex is the best","Alex","2023")

newB.displayinfoBook()

newFB = FictionBook(newB)

newFB.addGenre("Science Fiction")

newFB.addGenre("Historical Fiction")

newFB.whatGenres()



newNFB = NonFictionBook("Coding","Programming for dummies","Alex","2023")

newNFB.whatSubject()
        