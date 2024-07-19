# Python nested If else program to describe the interview process
round1 = input("Enter round1 result: ")
round2 = input("Enter round2 result: ")

if round1 == "passed":
    print("Congrats, first round is clear")
    if round2 == "passed":
        print("Congrats, second round is clear. You are placed")
    else:
        print("Sorry, please try next time")
else:
    print("Sorry, you did not get through first round. Please try next time ")