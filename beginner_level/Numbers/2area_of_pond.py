#In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
#1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. 
# Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

# given radius of the pond
r = 84

# value of pi
pi_value = 3.14

# calculating the area of the pond
area = pi_value * (r ** 2)

# water available per square meter
water_per_m2 = 1.4

# calculating total water in the pond
total_water = area * water_per_m2

# displaying the results
print("Area of pond:", area, "square meters")
print("Total water in pond:", int(total_water), "liters")