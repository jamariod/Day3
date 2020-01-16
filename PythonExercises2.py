"""
#Celsius to Fahrenheit
Celsius = float(input("Enter the temprtature in Celsius: ")) 
f = (Celsius*1.8) +32
print("Temperature in Farenheit is: ",f) """

#Tip Calculator
"""
total_bill_amount = float(input("Enter your total bill amount: "))

level_of_service = str(input("Is your level of service good, fair, or bad? "))

if (level_of_service == "good"):
    tip = .20
elif (level_of_service == "fair"):
    tip = .15
elif (level_of_service == "bad"):
    tip = .10

tip_calculator = (total_bill_amount * tip)
bill_total  = (total_bill_amount * tip) + total_bill_amount
print("Tip amount: $",format(tip_calculator, ",.2f"))
print("Total amount: $",format(bill_total, ",.2f"))"""

#Tip Calculator 2

total_bill_amount = float(input("Enter your total bill amount: "))

level_of_service = str(input("Is your level of service good, fair, or bad? "))

amount_of_people = int(input("Enter number of people: "))

if (level_of_service == "good"):
    tip = .20
elif (level_of_service == "fair"):
    tip = .15
elif (level_of_service == "bad"):
    tip = .10

tip_calculator = (total_bill_amount * tip)
bill_total  = (total_bill_amount * tip) + total_bill_amount
each_person_pays = bill_total/amount_of_people
print("Total amount: $",format(bill_total, ",.2f"))
print("Each person pay: $",format(each_person_pays, ",.2f"))
