#student results for three  subjects
name=input("enter student name:")
maths=int(input("enter your maths marks:"))
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))
if maths<35 or physics<35 or chemistry<35:
    print(f"the student {name} is failed")
else:
    print(f"the student {name} is passed")
    total=maths+physics+chemistry
    print(f"the total marks of {name} is : {total}")
    avg=total/3
    print(f"the avgerage marks of {name} is : {avg}")
    if avg > 70:
        print(f"the student {name} is in first class")
    elif avg >50:
        print(f"the student {name} is in second class")
    else:
        print(f"the student {name} is in third class")
    

