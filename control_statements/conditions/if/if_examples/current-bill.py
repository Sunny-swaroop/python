#current bill
meter_number=int(input("enter your meter number:"))
previous_reading=int(input("enter your previous reading:"))
current_reading=int(input("enter your current reading:"))
total_units=current_reading - previous_reading
print(f"this month total units is {total_units}")
if total_units==0:
    print(f"your meter {meter_number} has a problem,inform to service members")
else:
    if total_units <= 100:
        total_charge=2.50
        print(f"{meter_number} we are pricing {total_charge}rs for one unit")
    elif total_units <=150:
        total_charge=3.50
        print(f"{meter_number} we are pricing {total_charge}rs for one unit")
    elif total_units <=200:
        total_charge=4.50
        print(f"{meter_number} we are pricing {total_charge}rs for one unit")
    elif total_units <=300:
        total_charge=5.50
        print(f"{meter_number} we are pricing {total_charge}rs for one unit")
    else:
        total_charge=6.50
        print(f"{meter_number} we are pricing {total_charge}rs for one unit")
    total_amount=total_units*total_charge
    print(f"the current bill of this month is {total_amount}rs")

