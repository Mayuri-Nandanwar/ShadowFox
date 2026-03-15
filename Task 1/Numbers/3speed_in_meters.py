#If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. 
# Hint: Speed = Distance / Time

#Distance
distance_meters = 490

#Time
time_minutes = 7

#convert time in seconds
time_seconds = time_minutes * 60

#calculate peed in meters per second
Speed = distance_meters/time_seconds

#print the answer without any decimal point
print("Speed :", int(Speed), "meters per second")