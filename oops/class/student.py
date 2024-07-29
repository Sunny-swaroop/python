#how to create class
# class _"classname":
#this will create a class

class student:
    #the class is created
    def readdata(self): #this will prompt the user for input and then store that input in the instance attributes.
        self.name=input("enter the student name :")
        self.id=eval(input("enter the student-id :"))
        self.location=input("enter your area name :")
    def display(self): #to display the stored data, which is to print the data.
        print(f"student name : {self.name}")
        print(f"student id : {self.id}")
        print(f"student area name : {self.location}")

#final step we have to create a object and then we have to assign the class, attributes and also to display        
student=student()
student.readdata()
student.display()
        

