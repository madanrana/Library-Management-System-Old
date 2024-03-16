# users = []

# def add_user(name, user_id):
#     users.append({"name": name, "user_id": user_id})


# user.py

class User:
    """Represents a user in the library management system."""

    def __init__(self, name, user_id):
        """
        Initializes a user with a name and user ID.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: A string containing the user's name and ID.
        """
        return f"{self.name} (ID: {self.user_id})"

    def update(self, name=None, user_id=None):
        """
        Updates the user information.

        Args:
            name (str, optional): The new name of the user.
            user_id (str, optional): The new ID of the user.
        """
        if name:
            self.name = name
        if user_id:
            self.user_id = user_id

    def delete(self, library):
        """
        Deletes the user from the library.

        Args:
            library (Library): The library object.
        """
        library.remove_user(self)

    @staticmethod
    def search_by_name(library, name):
        """
        Searches for users by name in the library.

        Args:
            library (Library): The library object.
            name (str): The name to search for.

        Returns:
            list: A list of users with matching names.
        """
        return [user for user in library.users if user.name.lower() == name.lower()]

    @staticmethod
    def search_by_id(library, user_id):
        """
        Searches for users by ID in the library.

        Args:
            library (Library): The library object.
            user_id (str): The ID to search for.

        Returns:
            list: A list of users with the given ID.
        """
        return [user for user in library.users if user.user_id == user_id]
