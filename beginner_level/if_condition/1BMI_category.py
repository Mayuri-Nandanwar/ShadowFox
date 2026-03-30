#Write a program to determine the BMI Category based on user input. Ask the user to: Enter height in meters, Enter weight in kilograms, Calculate BMI using the formula: BMI = weight / (height)2
#Use the following categories: If BMI is 30 or greater, print "Obesity", If BMI is between 25 and 29, print "Overweight", If BMI is between 18.5 and 25, print "Normal"
#If BMI is less than 18.5, print "Underweight"
#Example: Enter height in meters: 1.75, Enter weight in kilograms: 70 Output: "Normal"

# taking input from user
h = float(input("Enter your height (in meters): "))
w = float(input("Enter your weight (in kg): "))

# calculating BMI
bmi_value = w / (h ** 2)

# checking BMI category
if bmi_value >= 30:
    print("Obesity")
elif bmi_value >= 25:
    print("Overweight")
elif bmi_value >= 18.5:
    print("Normal")
else:
    print("Underweight")