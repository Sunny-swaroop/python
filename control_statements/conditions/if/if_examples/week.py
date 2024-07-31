#checking week days
num=int(input("enter the number from 1 to 7 :"))
if num <= 0:
    print("its invalid")
else:
    if num==1:
        print(f"the {num} is Sunday")
    elif num==2:
        print(f"the {num} is monday")
    elif num==3:
        print(f"the {num} is tuesday")
    elif num==4:
        print(f"the {num} is wednsday")
    elif num==5:
        print(f"the {num} is thursday")
    elif num==6:
        print(f"the {num} is friday")
    elif num==7:
        print(f"the {num} is saturday")
    else:
        print(" its invalid number")
        

