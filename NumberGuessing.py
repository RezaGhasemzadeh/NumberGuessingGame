from random import randint
# We print the greetings and explain the game to the user.
print("----------------------Welcome to NumberGuessing game----------------------")
print("This game is very simple, I pick a number fom 1 to 100 and you should guess it in less than 10 rounds, otherwise"
      " you loose"
      "\nnow lets start the game")
# Here machine will produce a random number from 1 to 100 with randint method and random module.
computer_pick = randint(1, 100)
rounds = 10
while True:
    # In this loop we check every condition and calculate and display the number of rounds
    user_guess = int(input("what number I've picked?"))
    if user_guess > 100:
        print(f"broo! I told you from 1 to 100, {user_guess} is bigger than 100.")
        rounds -= 1
        # In these conditions we make deference between the users who have more than five rounds
        # and the users that have five or less than five rounds
        if rounds > 5:
            print(f"you have {rounds} rounds left")
        else:
            print(f"you have only {rounds} rounds left! be careful")
    elif user_guess < 1:
        print("from 1 to 100 this number is less than 1, guess again.")
        rounds -= 1
        if rounds > 5:
            print(f"you have {rounds} rounds left")
        else:
            print(f"you have only {rounds} rounds left! be careful")
    elif user_guess > computer_pick and (user_guess - computer_pick) >= 10:
        print("pick a lower number")
        rounds -= 1
        if rounds > 5:
            print(f"you have {rounds} rounds left")
        else:
            print(f"you have only {rounds} rounds left! be careful")
    elif user_guess > computer_pick and (user_guess - computer_pick) < 10:
        print("very close! a little lower.")
        rounds -= 1
        if rounds > 5:
            print(f"you have {rounds} rounds left")
        else:
            print(f"you have only {rounds} rounds left! be careful")
    elif user_guess < computer_pick and (computer_pick - user_guess) >= 10:
        print("pick a bigger number")
        rounds -= 1
        if rounds > 5:
            print(f"you have {rounds} rounds left")
        else:
            print(f"you have only {rounds} rounds left! be careful")
    elif user_guess < computer_pick and (computer_pick - user_guess) < 10:
        print("a little bigger will be okay")
        rounds -= 1
        if rounds > 5:
            print(f"you have {rounds} rounds left")
        else:
            print(f"you have only {rounds} rounds left! be careful")
    elif user_guess == computer_pick:
        # We print deferent messages for users who have won in five or more rounds and the users who have guessed in
        # less than five rounds
        if rounds >= 5:
            print(f"nice, you guessed the number only in {rounds} rounds!")
            break
        else:
            print(f"congratulations, to won but in fewer than 5 rounds, you won in {rounds} rounds.")
            break
    # if the user's input didn't match any of those conditions, we print this message
    else:
        print("you have entered a invalid value, try again")
        break
