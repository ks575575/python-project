class Library:                      # open with python this program
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books available in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 15 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

    def returnBook(self, num):
     for book in self.books:   
      if (num > str(15)):
         print("Return period is over. Please! pay the fine here")
         break
     else:
         print("You have returned the book in time.") 
    

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
    
    def returnBook(self):
        self.num = input("Enter the number of the days after you want to return: ")
        return self.num
         

if __name__ == "__main__":
    publicLibrary = Library(["The fault in our stars", "Django", "Clrs", "Python Notes","The Subconcious Mind","Rich Dad Poor Dad","Data Structures","DBMS","Discrete Maths","Android","Computer Architecture","Digital Electronics","Artificial intelligence","Internet of things","Machine Learning"])
    student = Student()
    # publicLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Public Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Pay Fine here
        5. Exit the Library
       
        
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            publicLibrary.displayAvailableBooks()
        elif a == 2:
            publicLibrary.borrowBook(student.requestBook())
        elif a == 3:
            publicLibrary.returnBook(student.returnBook())
        elif a == 4:
             publicLibrary.returnBook(student.returnBook()) 
        elif a == 5 :
            print("Thanks for choosing Public Library. Have a great day ahead!. Please visit again!!!")
        exit()

               
    else:

      print("Invalid Choice!")

        
