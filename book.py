# # Global list to store books
# books = []

# def add_book(title, author, isbn):
#     books.append({"title": title, "author": author, "isbn": isbn})

# def list_books():
#     for book in books:
#         print(book)

# book.py

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn):
        """
        Initializes a book with title, author, and ISBN.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: A string containing the book's title, author, and ISBN.
        """
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def update(self, title=None, author=None, isbn=None):
        """
        Updates the book information.

        Args:
            title (str, optional): The new title of the book.
            author (str, optional): The new author of the book.
            isbn (str, optional): The new ISBN of the book.
        """
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn

    def delete(self, library):
        """
        Deletes the book from the library.

        Args:
            library (Library): The library object.
        """
        library.remove_book(self)

    @staticmethod
    def search_by_title(library, title):
        """
        Searches for books by title in the library.

        Args:
            library (Library): The library object.
            title (str): The title to search for.

        Returns:
            list: A list of books with matching titles.
        """
        return [book for book in library.books if book.title.lower() == title.lower()]

    @staticmethod
    def search_by_author(library, author):
        """
        Searches for books by author in the library.

        Args:
            library (Library): The library object.
            author (str): The author to search for.

        Returns:
            list: A list of books by the given author.
        """
        return [book for book in library.books if book.author.lower() == author.lower()]

    @staticmethod
    def search_by_isbn(library, isbn):
        """
        Searches for books by ISBN in the library.

        Args:
            library (Library): The library object.
            isbn (str): The ISBN to search for.

        Returns:
            list: A list of books with the given ISBN.
        """
        return [book for book in library.books if book.isbn == isbn]
