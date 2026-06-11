class Library:
    
    def __init__(self, books):
        self.books = books
    
    def show_avail_books(self):
        print('Our Library Can Offer You The Following Books:')
        print('================================================')
        
        for book, borrower in self.books.items():
            if borrower == "Free":
                print(book)
        
    def lend_book(self, req_book, name):
        if self.books[req_book] == 'Free':
            self.books[req_book] = name
            print(f'{req_book} has been marked as Borrowed by: {name}')
            return True
        print(f'Sorry, the {req_book} is currently on loan to: {self.books[req_book]}')
        return False
    
    def return_book(self, returned_book):
        self.books[returned_book] = 'Free'
        print(f'Thanks for returning {returned_book}')
        
class Student:
    def __init__(self, name, library):
        self.name = name
        self.books = []
        self.library = library
        
    def view_borrowed(self):
        if not self.books:
            print('You have not borrowed any books')
        else:
            for book in self.books:
                print(book)
                
    def request_book(self):
        book = input('Enter the name of the book you would like to borrow: ')
        if self.library.lend_book(book, self.name):
            self.books.append(book)
            
    def return_book(self):
        book = input('Enter the name of the book you would like to return: ')
        if book in self.books:
            self.library.return_book(book)
            self.books.remove(book)
        else:
            print('You have not borrowed that book, try another.')
            
def create_lib():
    books = {
        'The Last Battle': 'Free',
        'The Hunger Games': 'Free',
        'Game of Thrones': 'Free',
        'Harry Potter 1': 'Free',
        'Harry Potter 2': 'Free',
        'Harry Potter 3': 'Free',
        'Harry Potter 4': 'Free',
        'Harry Potter 5': 'Free',
        'Harry Potter 6': 'Free',
        'Harry Potter 7': 'Free',
    }
    
    library = Library(books)
    stud = Student("Alice", library)
    
    while True:
        print('''
            ==========LIBRARY MENU===========
            1. Display Available Books
            2. Borrow a Book
            3. Return a Book
            4. View Your Books
            5. Exit
            ''')
        
        choice = input('Enter Choice: ')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                library.show_avail_books()
            elif choice == 2:
                stud.request_book()
            elif choice == 3:
                stud.return_book()
            elif choice == 4:
                stud.view_borrowed()
            elif choice == 5:
                print('Goodbye')
                raise SystemExit(0)
        else:
            print("Invalid Input. Try again")

if __name__ == '__main__':
    create_lib()