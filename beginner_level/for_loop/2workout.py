#Imagine you are doing a workout routine, and you have to complete 100 jumping jacks. Write a program that: Asks you to perform 10 jumping jacks at a time.
#After each set, it asks, "Are you tired?"

# total target
total_jacks = 100
done_jacks = 0

# doing workout in sets of 10
for i in range(10):
    done_jacks += 10
    print("You completed", done_jacks, "jumping jacks")

    # if goal is reached
    if done_jacks == total_jacks:
        print("Congratulations! You completed the workout.")
        break

    # asking user
    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()

        if skip in ["yes", "y"]:
            print("You completed a total of", done_jacks, "jumping jacks")
            break

    # showing remaining
    remaining = total_jacks - done_jacks
    print(remaining, "jumping jacks remaining")