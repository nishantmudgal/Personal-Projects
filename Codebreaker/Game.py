import random

# To get input from the user
def get_user_input():
    return list(input("Enter your guess : "))

#To generate a random code
def get_random_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

#To get the status of the input at each step
def return_status(input, random_code):
    if input == random_code:
        return "Congo! You WON"
    ret_list = []
    for index, inp in enumerate(input):
        if inp == random_code[index]:
            ret_list.append("Correct")
        elif inp in random_code:
            ret_list.append("IN list")
        else:
            ret_list.append("Not in list")
    return ret_list

#Run the actual game
def run_game():
    random_code = get_random_code()
    print("The random code is generated......")
    status = []
    steps = 0
    while "Congo! You WON" != status:
        input = get_user_input()
        status = return_status(input, random_code)
        print(status)
        steps = steps + 1
    print("You took " + str(steps) + " to crack the code")
    if steps < 3:
        print("You Are A PRO!!!!")
    elif steps < 7:
        print("You Played very well")
    else:
        print("Improve Your Logic Game")

#Here it starts
print("Welcome to most intersting game you ever played!!!!!!!")
run_game()
