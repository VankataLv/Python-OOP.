from typing import List


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []

    def info(self) -> str:
        return ', '.join(sorted(self.books))

    def __str__(self) -> str:
        return f"{self.user_id}, {self.username}, {self.books}"

    def add_book(self, new_book):
        self.books.append(new_book)


# user = User(1, 'Peter')
# user.add_book("Book C")
# user.add_book("Book B")
# user.add_book("Book A")
# print(user.info())
# # print(user)
# # print(user.books)
