from project.bookstore import Bookstore
from unittest import TestCase, main


class TestsBookstore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(100)

    def test_constructor(self):
        self.assertEqual(self.store.books_limit, 100)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {})
        self.assertEqual(self.store.total_sold_books, 0)

    def test_books_limit_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -1
        self.assertEqual(f"Books limit of -1 is not valid", str(ve.exception))

    def test_len_method(self):
        self.store.availability_in_store_by_book_titles = {"Book name": 10}
        expected_result = 10
        result = self.store.__len__()
        self.assertEqual(result, expected_result)

    def test_receive_book_book_limit_reached(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Book name", 101)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_enough_space(self):
        result = self.store.receive_book("Book name", 10)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"Book name": 10})
        expected_result = "10 copies of Book name are available in the bookstore."
        self.assertEqual(result, expected_result)

    def test_sell_book_unknown_book(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book name", 10)
        self.assertEqual("Book Book name doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_copies(self):
        self.store.receive_book("Book name", 10)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book name", 11)
        self.assertEqual("Book name has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_book_good_data(self):
        self.store.receive_book("Book name", 20)
        result = self.store.sell_book("Book name", 10)
        expected_result = "Sold 10 copies of Book name"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"Book name": 10})
        self.assertEqual(self.store.total_sold_books, 10)

    def test__str__no_books(self):
        result = self.store.__str__()
        expected_result_data = [f"Total sold books: {self.store.total_sold_books}",
                                f'Current availability: {len(self.store)}']
        for book_title, number_of_copies in self.store.availability_in_store_by_book_titles.items():
            expected_result_data.append(f" - {book_title}: {number_of_copies} copies")
        expected_result = '\n'.join(expected_result_data)
        self.assertEqual(result, expected_result)

    def test__str__with_books(self):
        self.store.receive_book("Book name", 20)

        result = self.store.__str__()
        expected_result_data = [f"Total sold books: {self.store.total_sold_books}",
                                f'Current availability: {len(self.store)}']
        for book_title, number_of_copies in self.store.availability_in_store_by_book_titles.items():
            expected_result_data.append(f" - {book_title}: {number_of_copies} copies")
        expected_result = '\n'.join(expected_result_data)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()