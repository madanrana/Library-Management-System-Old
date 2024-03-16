import unittest
from library import Library
from book import Book
from user import User
from check import Check
from storage import Storage

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_check_out(self):
        book = Book("Test Book", "Test Author", "1234567890")
        user = User("Test User", "001")
        self.library.add_book(book)
        self.library.add_user(user)
        Check.check_out(self.library, user, book)  # Use Check.check_out method
        self.assertEqual(book.checked_out_by, user)

    def test_check_in(self):
        book = Book("Test Book", "Test Author", "1234567890")
        user = User("Test User", "001")
        self.library.add_book(book)
        self.library.add_user(user)
        Check.check_out(self.library, user, book)  # Check out the book first
        Check.check_in(self.library, book)  # Use Check.check_in method
        self.assertIsNone(book.checked_out_by)

    def test_save_and_load_books(self):
        filename = "test_books.json"
        book1 = Book("Test Book 1", "Test Author", "1234567890")
        book2 = Book("Test Book 2", "Test Author", "0987654321")
        self.library.add_book(book1)
        self.library.add_book(book2)
        Storage.save_books(self.library.books, filename)
        loaded_books = Storage.load_books(filename)
        self.assertEqual(len(loaded_books), 2)
        self.assertTrue(any(book.title == "Test Book 1" for book in loaded_books))
        self.assertTrue(any(book.title == "Test Book 2" for book in loaded_books))

    def test_save_and_load_users(self):
        filename = "test_users.json"
        user1 = User("Test User 1", "001")
        user2 = User("Test User 2", "002")
        self.library.add_user(user1)
        self.library.add_user(user2)
        Storage.save_users(self.library.users, filename)
        loaded_users = Storage.load_users(filename)
        self.assertEqual(len(loaded_users), 2)
        self.assertTrue(any(user.name == "Test User 1" for user in loaded_users))
        self.assertTrue(any(user.name == "Test User 2" for user in loaded_users))

    def tearDown(self):
        # Clean up after each test
        pass

if __name__ == '__main__':
    unittest.main()
