# create a student class 
class Student:
  def __init__(self, name, age):
    self.name = name 
    self.age = age 
    
  def display_studentInfo(self):
    return f"Student Name: {self.name}\nStudent Age: {self.age}"
  
  
# create instance (object) for class 
student1 = Student('Alice', 23)
student2 = Student('Nathan', 58)

# usage of the method
print(student1.display_studentInfo())
print(student2.display_studentInfo())


