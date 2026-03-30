#Write a program to determine which country a city belongs to. Given list of cities per country: Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
#UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#Ask the user to enter a city name and print the corresponding country. Example: Enter a city name: "Abu Dhabi" Output: "Abu Dhabi is in UAE"

# list of cities for each country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# taking input from user
city_name = input("Enter a city name: ")

# checking which country the city belongs to
if city_name in australia:
    print(city_name, "is in Australia")
elif city_name in uae:
    print(city_name, "is in UAE")
elif city_name in india:
    print(city_name, "is in India")
else:
    print("City not found in the list")
       