# main.py
from library import Library
from book import Book
from user import User

def print_books(books):
    """Prints a list of books."""
    if books:
        print("Books in Library:")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
    else:
        print("No books in the library.")

def print_users(users):
    """Prints a list of users."""
    if users:
        print("Users in Library:")
        for i, user in enumerate(users, 1):
            print(f"{i}. {user}")
    else:
        print("No users in the library.")

def main():
    library = Library()

    while True:
        print("\n1. Add Book\n2. Remove Book\n3. Add User\n4. Remove User\n"
              "5. List Books\n6. List Users\n7. Search Books\n8. Search Users\n"
              "9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            print_books(library.books)
            if library.books:
                try:
                    index = int(input("Enter the number of the book to remove: ")) - 1
                    book = library.books[index]
                    library.remove_book(book)
                    print("Book removed successfully.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number.")
        
        elif choice == '3':
            name = input("Enter name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)
            library.add_user(user)
            print("User added successfully.")

        elif choice == '4':
            print_users(library.users)
            if library.users:
                try:
                    index = int(input("Enter the number of the user to remove: ")) - 1
                    user = library.users[index]
                    library.remove_user(user)
                    print("User removed successfully.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number.")

        elif choice == '5':
            print_books(library.books)

        elif choice == '6':
            print_users(library.users)

        elif choice == '7':
            search_criteria = input("Enter search criteria (title/author/isbn): ")
            search_term = input("Enter search term: ")
            if search_criteria.lower() == 'title':
                results = Book.search_by_title(library, search_term)
            elif search_criteria.lower() == 'author':
                results = Book.search_by_author(library, search_term)
            elif search_criteria.lower() == 'isbn':
                results = Book.search_by_isbn(library, search_term)
            else:
                print("Invalid search criteria.")
                continue

            print_books(results)

        elif choice == '8':
            search_criteria = input("Enter search criteria (name/id): ")
            search_term = input("Enter search term: ")
            if search_criteria.lower() == 'name':
                results = User.search_by_name(library, search_term)
            elif search_criteria.lower() == 'id':
                results = User.search_by_id(library, search_term)
            else:
                print("Invalid search criteria.")
                continue

            print_users(results)

        elif choice == '9':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()
