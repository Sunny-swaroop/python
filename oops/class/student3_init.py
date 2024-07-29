#using init constructor
#3rd example
#assining the values from the user, using init constructor
class student :
    def __init__(self,x,y,z):
        self.name=x
        self.id=y
        self.location=z
    def display(self):
        print(f"enter student name :{self.name}")
        print(f"enter student id :{self.id}")
        print(f"enter student location :{self.location}")
#when we are creating an instance we can pass the values to the attributes
student=student("sunny",1234,"hyderabad")
student.display()


