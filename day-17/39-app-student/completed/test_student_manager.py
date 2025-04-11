import unittest
from student_manager import StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()

    def test_add_student(self):
        s = self.manager.add_student("John", 18, "C")
        self.assertEqual(s.name, "John")

    def test_find_by_id(self):
        s = self.manager.add_student("Jane", 19, "B")
        found = self.manager.find_by_id(s.id)
        self.assertEqual(found.name, "Jane")

    def test_delete_student(self):
        s = self.manager.add_student("Tom", 17, "D")
        self.assertTrue(self.manager.delete_student(s.id))
        self.assertIsNone(self.manager.find_by_id(s.id))
