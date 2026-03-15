#In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
#1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. 
# Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

#radius of pond
radius = 84

#value of pie
pi = 3.14

#calculate area of pond
pond_area = pi * (radius ** 2)

# Water per square meter 
water_per_square_meter = 1.4

# Total water in the pond 
total_water = pond_area * water_per_square_meter

# Print results
print("Area of the pond:", pond_area, "square meters")

# Print water amount without any decimal point
print("Total water in the pond:", int(total_water), "liters")