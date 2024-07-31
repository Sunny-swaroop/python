#student results for three  subjects
name=input("enter student name:")
maths=int(input("enter your maths marks:"))
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))
if maths<35 or physics<35 or chemistry<35:
    print(f"the student {name} is failed")
else:
    result="pass"
    total=maths+physics+chemistry
    avg=total/3
    if avg > 60:
        grade="first"
    elif avg >50:
        grade="second"
    else:
        grade="third"
    print(f"the student {name} is {result}")
    print(f"the student {name} total is :{total}")
    print(f"the student {name} avg is :{avg}")
    print(f"the grade is {grade}")
    
