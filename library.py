# library.py
from book import Book
from user import User

class Library:
    """Represents a library management system."""

    def __init__(self):
        """Initializes a library with empty lists of books and users."""
        self.books = []
        self.users = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The book object to add.
        """
        self.books.append(book)

    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
            book (Book): The book object to remove.
        """
        self.books.remove(book)

    def add_user(self, user):
        """
        Adds a user to the library.

        Args:
            user (User): The user object to add.
        """
        self.users.append(user)

    def remove_user(self, user):
        """
        Removes a user from the library.

        Args:
            user (User): The user object to remove.
        """
        self.users.remove(user)
