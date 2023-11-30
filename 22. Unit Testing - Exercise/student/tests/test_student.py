from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):

    def setUp(self) -> None:
        self.std1 = Student("Ivan")
        self.std2 = Student("Petar", {"Python": ["n1", "n2", "n3"]})

    def test_constructor(self):
        self.assertEqual(self.std1.name, "Ivan")
        self.assertEqual(self.std1.courses, {})

        self.assertEqual(self.std2.name, "Petar")
        self.assertEqual(self.std2.courses, {"Python": ["n1", "n2", "n3"]})

    def test_enroll_if_course_already_exists(self):
        expected_return = "Course already added. Notes have been updated."
        result = self.std2.enroll("Python", ["n4", "n5"], "Y")
        self.assertEqual(expected_return, result)

        courses_expected = {"Python": ["n1", "n2", "n3", "n4", "n5"]}
        self.assertEqual(courses_expected, self.std2.courses)

    def test_enroll_if_new_course_has_notes_to_add(self):
        expected_return = "Course and course notes have been added."
        result = self.std1.enroll("JS", ["n4", "n5"], "Y")
        self.assertEqual(expected_return, result)

        courses_expected = {"JS": ["n4", "n5"]}
        self.assertEqual(courses_expected, self.std1.courses)

    def test_enroll_if_new_course_does_not_have_notes_to_add(self):
        expected_return = "Course has been added."
        result = self.std1.enroll("JS", [], "N")
        self.assertEqual(expected_return, result)

        courses_expected = {"JS": []}
        self.assertEqual(courses_expected, self.std1.courses)

    def test_add_notes_valid_course(self):
        result = self.std2.add_notes("Python", "added_note")
        courses_expected = {"Python": ["n1", "n2", "n3", "added_note"]}
        self.assertEqual(courses_expected, self.std2.courses)
        self.assertEqual("Notes have been updated", result)

    def test_enroll_not_valid_course(self):
        with self.assertRaises(Exception) as ex:
            self.std2.add_notes("JS", ["n1", "n99"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_existing_course(self):
        result = self.std2.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.std2.courses)

    def test_leave_course_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.std2.leave_course("C++")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
