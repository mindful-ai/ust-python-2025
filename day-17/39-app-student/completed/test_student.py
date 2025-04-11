import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_create_student(self):
        s = Student("Alice", 20, "A")
        self.assertEqual(s.name, "Alice")
        self.assertEqual(s.age, 20)
        self.assertEqual(s.grade, "A")

    def test_dict_conversion(self):
        s = Student("Bob", 21, "B")
        d = s.to_dict()
        s2 = Student.from_dict(d)
        self.assertEqual(s.id, s2.id)
