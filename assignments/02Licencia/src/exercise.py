age = int(input("Enter your age: "))
id = input("Do you have identification? ")

if age == 18 and id == 'yes':
 print("Licensing procedure granted.")
elif (age < 18 and age >= 0) or id == 'no':
 print ("You don´t meet the requirements.")
else:
 print ("Wrong answer.")
