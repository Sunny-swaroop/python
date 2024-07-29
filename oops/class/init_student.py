#using constructor
#__init__ is a constructor, It is a special method used to initialize an instance of a class.
#we can take student class as an example
class student :
    def __init__(self):
        self.name="sunny"
        self.id=1234
        self.location="hyderabad"
    def display(self):
        print(f"student name is :{self.name}")
        print(f"student id is :{self.id}")
        print(f"student address is :{self.location}")

#here we are creating an instance of an object
student=student()
#we are calling display method on the instance
student.display()

