def imc(height,weight):
  
    return weight/height**2

weight=float(input("Weight in kilograms: "))
height=float(input("Height in meters: "))

if index >= 0 and imc <= 15.99
        print ("Severe thinness")
    elif imc >= 16.00 and imc <= 16.99
        print ("Moderate thinness")
    elif imc >= 17.00 and imc <= 18.49
        print ("Slight thinness")
    elif imc >= 18.50 and imc <= 24.99
        print ("Normal")
    elif imc >= 25.00 and imc <= 29.99
        print ("Overweight")
    elif imc >= 30.00 and imc <= 34.99
        print ("Mild obesity")
    elif imc >= 35.00 and imc <= 39.00
        print ("Medium obesity")
    elif imc >= 40.00
        print ("Morbid obesity")

index=imc(height,weight)

print("Your BMI is: {}".format(index))
print("Your weight in kg is: {}".format(weight))
print("Your height in m is: {}".format(height))
