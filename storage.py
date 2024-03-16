# storage.py
import json
from book import Book
from user import User


class Storage:
    """Handles file-based storage operations for the library data."""

    @staticmethod
    def save_books(books, filename):
        """
        Saves a list of books to a JSON file.

        Args:
            books (list): The list of book objects to save.
            filename (str): The name of the JSON file.
        """
        data = [{"title": book.title, "author": book.author, "isbn": book.isbn} for book in books]
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_books(filename):
        """
        Loads a list of books from a JSON file.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            list: A list of book objects loaded from the file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                books = [Book(book['title'], book['author'], book['isbn']) for book in data]
            return books
        except FileNotFoundError:
            return []

    @staticmethod
    def save_users(users, filename):
        """
        Saves a list of users to a JSON file.

        Args:
            users (list): The list of user objects to save.
            filename (str): The name of the JSON file.
        """
        data = [{"name": user.name, "user_id": user.user_id} for user in users]
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_users(filename):
        """
        Loads a list of users from a JSON file.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            list: A list of user objects loaded from the file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                users = [User(user['name'], user['user_id']) for user in data]
            return users
        except FileNotFoundError:
            return []
