from extended_list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):

    def setUp(self):
        self.lst = IntegerList(1, 2, 3, "wrong", True, 55.5)

    def test_constructor(self):
        self.assertEqual([1, 2, 3], self.lst.get_data())

    def test_add_with_int(self):
        expected_result = [1, 2, 3, 4]

        self.lst.add(4)

        self.assertEqual(self.lst.get_data(), expected_result)

    def test_add_with_non_int(self):
        with self.assertRaises(ValueError) as ve:
            self.lst.add("wrong_format")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_valid_index(self):
        expected_result = [1, 2]

        removed_num = self.lst.remove_index(2)

        self.assertEqual(expected_result, self.lst.get_data())
        self.assertEqual(3, removed_num)

    def test_remove_index_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.lst.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index(self):
        expected_num = 1
        self.assertEqual(expected_num, self.lst.get(0))

    def test_get_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.lst.get(55)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.lst.insert(55, 10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_el_float(self):
        with self.assertRaises(ValueError) as ve:
            self.lst.insert(1, 55.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_attributes(self):
        expected_result = [1, 55, 2, 3]
        self.lst.insert(1, 55)

        self.assertEqual(expected_result, self.lst.get_data())

    def test_get_biggest(self):
        expected_num = 55
        self.lst.insert(0, expected_num)

        self.assertEqual(expected_num, self.lst.get_biggest())

    def test_get_index(self):
        index_searched = 0
        self.assertEqual(index_searched, self.lst.get_index(1))


if __name__ == "__main__":
    main()
