import uuid
class Student:
    def __init__(self, name, age, grade, student_id=None):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        else:
            self.name = name
        self.id = student_id or str(uuid.uuid4())
        self.age = age
        self.grade = grade
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
    @staticmethod
    def from_dict(data):
        return Student(
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            student_id=data["id"]
        )
        
if __name__ == "__main__":
    s = Student("abc",25,"a")