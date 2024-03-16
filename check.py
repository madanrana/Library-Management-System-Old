# check.py
from datetime import datetime

class Check:
    """Represents book check-in and check-out operations."""

    @staticmethod
    def check_out(library, user, book):
        """
        Checks out a book from the library.

        Args:
            library (Library): The library object.
            user (User): The user checking out the book.
            book (Book): The book to be checked out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if book in library.books:
            library.books.remove(book)
            book.checked_out_by = user
            book.checkout_date = datetime.now()
            return True
        else:
            print("Book not available for checkout.")
            return False

    @staticmethod
    def check_in(library, book):
        """
        Checks in a book to the library.

        Args:
            library (Library): The library object.
            book (Book): The book to be checked in.
        """
        library.books.append(book)
        book.checked_out_by = None
        book.checkout_date = None
