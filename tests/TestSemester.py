import unittest

from pyutttils.Semester import Semester


class TestSemester(unittest.TestCase):

    def test_semester(self):
        self.assertEqual(Semester("P22").full_name, "Printemps 2022")

    def test_semester_next(self):
        self.assertEqual(Semester("P22").get_next().full_name, "Automne 2022")

    def test_semester_previous(self):
        self.assertEqual(Semester("P22").get_previous().full_name, "Automne 2021")


if __name__ == '__main__':
    unittest.main()