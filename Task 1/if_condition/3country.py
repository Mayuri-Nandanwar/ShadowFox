#Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.
#Example: Enter the first city: "Mumbai", Enter the second city: "Chennai" Output: "Both cities are in India" Example: Enter the first city: "Sydney"
#Enter the second city: "Dubai" Output: "They don't belong to the same country"

#list of cities
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

#Ask user to enter a city name
City1 = input("Enter the first city name :")
City2 = input("Enter the second city name :")

#Check whether they belong to the same country or not.
if City1 in India and City2 in India:
    print("Both cities are in India.")
elif City1 in Australia and City2 in Australia:
    print("Both cities are in Australia.")
elif City1 in UAE and City2 in UAE:
    print("Both cities are in UAE.")
else:
    print("They don't belong to the same country.")