#Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times). Count and print the following statistics: How many times you rolled a 6
#How many times you rolled a 1, How many times you rolled two 6s in a row

import random

#number of times the die is rolled
total_throws = 20

#Counters
count_six = 0
count_one = 0
double_six_count = 0
previous_roll = None

# Simulate die rolls
for attempt in range(total_throws):
    roll = random.randint(1, 6)
    print("Roll", attempt+1, ":", roll)
    
    if roll == 6:
        count_six += 1
    if roll == 1:
        count_one += 1
    if roll == 6 and previous_roll == 6:
        previous_roll += 1
    previous_roll = roll
    
 #print statistics   
print("\n Statistics:")
print("Times 6 appeared :", count_six)
print("Times 1 appeared :", count_one)
print("Times two 6s came in a row :", double_six_count)



