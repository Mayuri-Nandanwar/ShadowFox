#Imagine you are doing a workout routine, and you have to complete 100 jumping jacks. Write a program that: Asks you to perform 10 jumping jacks at a time.
#After each set, it asks, "Are you tired?"

#Total target of jumping jacks
target_jump = 100
complete_jump = 0

#perform 10 jumping jacks at a time
for round_count in range(10):
    complete_jump += 10
    print("You completed", complete_jump, "jumping jacks.")
    
    #If 100 jumps are completed, stop
    if complete_jump == target_jump:
        print("Congratulations! you completed the workout.")
        break
    User_tired = input("are you tired? (Yes\Y or No\n): ")
    if User_tired == "Yes" or User_tired == "Y":
        skip = input("Do you want to skip the remaining sets? (Yes\Y or No\n): ")
        
        if skip == "Yes" or skip == "Y":
            print("You completed a total of", complete_jump, "jumping jacks. ")
            break
        else:
            ramaining_jacks = target_jump - complete_jump
            print(remaining_jacks, "jumping jacks remaining. ")
            
    else:
        remaining_jacks = target_jump -complete_jump
        print(remaining_jacks, "jumping jacks remaining. ")
            