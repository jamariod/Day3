#name = input('What is your name? ')

#Print the user's name in ALL CAPS, and also tell them the number of letters in their name.
#name = input('What is your name? ')
#print(len(name.upper()))

#Madlib 
"""
name = input("Enter your name: ")
subject = input("Enter your subject: ")
print(name + "'s favorite subject in school is " + subject + ".")

def greater_than_1(n):
   return n > 1
print(greater_than_1(1))

None is return
def no_expression_list():
   return #No return expression list.
print(no_expression_list())

def return_two_values():
    a = 40
    b = 2
    return a,b
print("First value = %d, Second value = %d" %(return_two_values())) """


day = int(input('Day (0-6)?'))

Mon = 0
if day == 0:
  print("Mon")
if day == 1:
  print("Tues")
if day == 2:
    print("Wed")
if day == 3:
    print("Thurs")
if day == 4:
    print("Fri")
if day == 5:
    print("Sat")
if day == 6:
    print("Sun")

if day >= 4:
    print("Sleep in")
else:
    print("Go to work")




