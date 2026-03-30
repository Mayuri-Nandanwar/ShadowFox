#Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times). Count and print the following statistics: How many times you rolled a 6
#How many times you rolled a 1, How many times you rolled two 6s in a row

import random

# total number of throws
throws = 20

# counters
six_count = 0
one_count = 0
consecutive_six = 0

last_roll = None

# rolling the die
for i in range(throws):
    value = random.randint(1, 6)
    print("Roll", i + 1, ":", value)

    if value == 6:
        six_count += 1
    if value == 1:
        one_count += 1

    # check for two 6s in a row
    if value == 6 and last_roll == 6:
        consecutive_six += 1

    last_roll = value

# printing results
print("\nStatistics:")
print("Number of times 6 appeared:", six_count)
print("Number of times 1 appeared:", one_count)
print("Number of times two 6s in a row:", consecutive_six)