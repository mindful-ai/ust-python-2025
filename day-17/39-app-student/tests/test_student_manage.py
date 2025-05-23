import unittest
from student_manager import StudentManager

class TestCasesForStudent(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManager()
    
    def test_add_student(self):
        name = "anil"
        age  = "12"
        grade = "6"
        nstudents = self.manager.students
        self.manager.add_student(name, age, grade)
        self.assertEqual(len(self.manager.students), nstudents + 1)
        self.assertEqual(self.manager.students[nstudents+1].name, name)
        self.assertEqual(self.manager.students[nstudents+1].age, age)
        self.assertEqual(self.manager.students[nstudents+1].grade, grade)

    def tearDown(self):
        return super().tearDown()