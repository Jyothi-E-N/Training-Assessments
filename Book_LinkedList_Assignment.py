[09:30] Busanaboina, Indhira

class Book:

    def __init__(self, id, title, author, price, rating, next=None):

        self.id =id

        self.title = title

        self.author= author

        self.price = price

        self.rating = int(rating)

        self.next = next

 

class LinkedList_book:

    def __init__(self):

        self.first = None

 

    def addBooks(self, book):

        if not self.first:

            self.first = book

        else:

            current_node = self.first

            while current_node.next:

                current_node = current_node.next

            current_node.next = book

 

    def findBookByID(self, id):

        current_node = self.first

        while current_node:

            if current_node.id == id:

                return current_node

            current_node = current_node.next

        return False

   

    def findBooksByAuthor(self, author):

        list_books = list()

        current_node = self.first

        while current_node:

            if current_node.author == author:

                list_books.append(current_node)

            current_node = current_node.next

        return list_books

   

    def findBooksByRating(self, min_rating, max_rating):

        list_books = list()

        current_node = self.first

        while current_node:

            if current_node.rating>=min_rating and current_node.rating<= max_rating:

                list_books.append(current_node)

            current_node = current_node.next

        return list_books

   

    def findBooksByPrice(self, min_price, max_price):

        list_book = list()

        current_node = self.first

        while current_node:

            if current_node.price >= min_price and current_node.price <= max_price:

                list_book.append(current_node)

            current_node=current_node.next

        return list_book

 

   

    def display_books(self):

        current_book = self.first

        while current_book:

            print(f"Book ID: {current_book.id}, Title of the Book: {current_book.title}, Author: {current_book.author}, Price: {current_book.price}, Rating: {current_book.rating}")

            current_book = current_book.next

   

 

if __name__ == "__main__":

    BookData = LinkedList_book()

    Book1  = Book(1,"Ramayan","Valmiki",5000, 5)

    Book2  = Book(2,"Mahabharath","Vedvyas",6000, 5)

    Book3  = Book(3, "Wings of Fire", "APJ Abdul Kalam", 365 ,4.5)

    Book4  = Book(4, "Ignited Minds", "APJ Abdul Kalam", 263 ,3)

 

    BookData.addBooks(Book1)

    BookData.addBooks(Book2)

    BookData.addBooks(Book3)

    BookData.addBooks(Book4)

    id = 3

    found_book = BookData.findBookByID(id)

    if found_book:

        print(f"\nBook with ID:{found_book.id} is {found_book.title}", end="")

    else:

        print(f"Book with {id} is Not found")

    print("\n")

    print("*"*100)

 

    author = "APJ Abdul Kalam"

    found_book_a = BookData.findBooksByAuthor(author)

    if found_book_a:

        print(f"Books by {author} are", end=":\t")

        for buk in found_book_a:        

            print(f"{buk.title}", end="\t")

    else:

        print("No books found")

   

    print("\n")

    print("*"*100)

 

    min_rating = 4

    max_rating = 5

    found_book=BookData.findBooksByRating(int(min_rating), int(max_rating))

    if found_book:

        print(f"Books with rating between {min_rating} and {max_rating} are: ", end="\t")

        for buk in found_book:

            print(f"{buk.title}", end = "\t")

    else:

        print("books not found")

 

    print("\n")

    print("*"*100)

 

    min_price = 200

    max_price = 1000

    found_book=BookData.findBooksByPrice(min_price, max_price)

    if found_book:

        print(f"Books with prices between {min_price} and {max_price} are: ", end="\t")

        for buk in found_book:

            print(f"{buk.title}", end = "\t")

    else:

        print("books not found")

 

    print("\n")

    print("*"*100)

   

   

    BookData.display_books()

   
