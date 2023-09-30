from getRandomWord import gameWord4, gameWord5, gameWord6

def wordleGame4():
    global gameWord4
    gameWord = gameWord4.lower()
    attempts = 6

    print(f"You have {attempts} attempts\n")

    while attempts > 0:
        userGuess = str(input("Please guess your word: "))
        userGuess = userGuess.lower()
        if len(userGuess) == 4:
            if userGuess == gameWord:
                turnsToWin = 7 - attempts
                if turnsToWin == 1:
                    print(f"Congratulations!\nYou won in {turnsToWin} attempt.")
                    return
                elif turnsToWin > 1:
                    print(f"Congratulations!\nYou won in {turnsToWin} attempts.")
                    return
            else:
                attempts -= 1
                print("That was an incorrect guess")
                for char, word in zip(gameWord, userGuess):
                    if word in gameWord and word in char:
                        print(f"{word} - ✔")
                    elif word in gameWord:
                        print(f"{word} - ➕")
                    else:
                        print(f"{word} - ❌")
                if attempts > 0:
                    print(f"You have {attempts} attempts left. Guess again")
                else:
                    print(f"Unlucky, the word was {gameWord}")
        elif len(userGuess) < 4:
            print(
                "The word you have entered has less than 4 characters. Please only enter 4 character words."
            )
        elif len(userGuess) > 4:
            print(
                "The word you have entered has more than 4 characters. Please only enter 4 character words."
            )

def wordleGame5():
    global gameWord5
    gameWord = gameWord5.lower()
    attempts = 6

    print(f"You have {attempts} attempts\n")

    while attempts > 0:
        userGuess = str(input("Please guess your word: "))
        userGuess = userGuess.lower()
        if len(userGuess) == 5:
            if userGuess == gameWord:
                turnsToWin = 7 - attempts
                if turnsToWin == 1:
                    print(f"Congratulations!\nYou won in {turnsToWin} attempt.")
                    return
                elif turnsToWin > 1:
                    print(f"Congratulations!\nYou won in {turnsToWin} attempts.")
                    return
            else:
                attempts -= 1
                print("That was an incorrect guess")
                for char, word in zip(gameWord, userGuess):
                    if word in gameWord and word in char:
                        print(f"{word} - ✔")
                    elif word in gameWord:
                        print(f"{word} - ➕")
                    else:
                        print(f"{word} - ❌")
                if attempts > 0:
                    print(f"You have {attempts} attempts left. Guess again")
                else:
                    print(f"Unlucky, the word was {gameWord}")
        elif len(userGuess) < 5:
            print(
                "The word you have entered has less than 5 characters. Please only enter 5 character words."
            )
        elif len(userGuess) > 5:
            print(
                "The word you have entered has more than 5 characters. Please only enter 5 character words."
            )

def wordleGame6():
    global gameWord6
    gameWord = gameWord6.lower()
    attempts = 6

    print(f"You have {attempts} attempts\n")

    while attempts > 0:
        userGuess = str(input("Please guess your word: "))
        userGuess = userGuess.lower()
        if len(userGuess) == 4:
            if userGuess == gameWord:
                turnsToWin = 7 - attempts
                if turnsToWin == 1:
                    print(f"Congratulations!\nYou won in {turnsToWin} attempt.")
                    return
                elif turnsToWin > 1:
                    print(f"Congratulations!\nYou won in {turnsToWin} attempts.")
                    return
            else:
                attempts -= 1
                print("That was an incorrect guess")
                for char, word in zip(gameWord, userGuess):
                    if word in gameWord and word in char:
                        print(f"{word} - ✔")
                    elif word in gameWord:
                        print(f"{word} - ➕")
                    else:
                        print(f"{word} - ❌")
                if attempts > 0:
                    print(f"You have {attempts} attempts left. Guess again")
                else:
                    print(f"Unlucky, the word was {gameWord}")
        elif len(userGuess) < 6:
            print(
                "The word you have entered has less than 6 characters. Please only enter 6 character words."
            )
        elif len(userGuess) > 6:
            print(
                "The word you have entered has more than 6 characters. Please only enter 6 character words."
            )

def gameInstruction():
    print("Wordle is a game where you will be given 6 attempts to guess a word.")
    print(
        "✔ - The letter is in the word and in the correct spot\n➕ - The letter is in the word but not in the correct spot\n❌ - The letter is not in the word"
    )
    def chooseGamemode():
        gameModeChoice = input("Would you like to play with a 4, 5 or 6 letter word?\nEnter 4, 5 or 6: ")
        if gameModeChoice == "4":
            wordleGame4()
        elif gameModeChoice == "5":
            wordleGame5
        elif gameModeChoice == "6":
            wordleGame6
        else:
            print("Unrecognised gamemode.")
            chooseGamemode()
    chooseGamemode()



gameInstruction()