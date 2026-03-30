#If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. 
# Hint: Speed = Distance / Time

# given distance in meters
distance = 490

# time taken in minutes
time_min = 7

# converting time into seconds
time_sec = time_min * 60

# calculating speed (m/s)
speed = distance / time_sec

# displaying the result without decimal
print("Speed:", int(speed), "meters per second")