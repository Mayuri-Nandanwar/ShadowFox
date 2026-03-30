#Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.
#Example: Enter the first city: "Mumbai", Enter the second city: "Chennai" Output: "Both cities are in India" Example: Enter the first city: "Sydney"
#Enter the second city: "Dubai" Output: "They don't belong to the same country"

# lists of cities
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# taking input from user
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

# checking if both cities belong to the same country
if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
else:
    print("They don't belong to the same country")