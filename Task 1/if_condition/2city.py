#Write a program to determine which country a city belongs to. Given list of cities per country: Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
#UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#Ask the user to enter a city name and print the corresponding country. Example: Enter a city name: "Abu Dhabi" Output: "Abu Dhabi is in UAE"

#list of cities
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

#Ask user to enter a city name
City = input("Enter a city name :")

if City in Australia:
    print(City, "is in Australia.")
elif City in UAE:
    print(City, "is in UAE.")
elif City in India:
    print("is in India.")
else:
    print("City is not found in list.")
       