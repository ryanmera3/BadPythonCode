import random

def selectionMenu(playerName):
    #Starts balance at 100 and welcomes the player
    playerBalance = 100
    print("Welcome to the Retro Arcade " + str(playerName) + ".")

    done = False
    #Loops as long as the players balance is higher than 0 and the player isn't finished playing
    while playerBalance > -1 and done == False:
        print("Choose a game from the following options or quit. ")
        print("(D)ice | -10 credits")
        print("(S)lots | -10 credits")
        print("(M)adlibs | +20 credits")
        print("(Q)uit")
        print("(P)layerBalance")
        question = input("Which game do you want to play?: ")



        # If input is D then it chooses Dice game | Subtracts 10 credits
        if  question == ("D") and playerBalance > 0:
            print("You've chosen the Dice game.")
            playerBalance-=10
            playGameOfDice(playerName)

        #If input is S then it chooses Slots | Subtracts 10 credits
        elif question == ("S") and playerBalance > 0:
            print("You've chosen Slots.")
            playerBalance-=10
            playGameOfSlots(playerName)

        #If input is M then it chooses Madlibs | Adds 20 credits
        elif question == ("M"):
            print("You've chosen Madlibs.")
            playerBalance+=20
            createMadlib(playerName)

        #If input is Q then it Quits the game
        elif question == ("Q") and playerBalance > 0:
            print("Thanks for playing.")
            exit()

        #If input is P then it shows the players remaining balance
        elif question == ("P"):
            print("Your remaining balance is "+ str(playerBalance)+ ".")

        elif playerBalance == 0 and question != ("M"):
            print("You don't have enough credits to play this game. ")

        #Keeps the loop going if they enter something other than the available options
        else:
            done = False

# Function that allows you to enter your name then rolls dice vs a computer and tracks points - First to 5 wins
def playGameOfDice(playerName):

    #Welcomes player to the game and starts at 0 score
    print("Welcome to the Dice game " + str(playerName))
    computerScore = 0
    playerScore = 0

    winner = False

    #Keeps the loop going until the player or computer hits 5
    while winner == False:

        #Decides winner / first to 5 points - Player wins
        if playerScore == 5:
            print("You have gained 5 points and win the game! ")
            winner = True

        #Decides winner / first to 5 points - Computer wins
        elif computerScore == 5:
            print("The house has gained 5 points. You lose. ")
            winner = True

        #Dice roll variables
        playerResult = random.randint(1, 6)
        computerResult = random.randint(1, 6)
        diceDisplay(playerResult)
        diceDisplay(computerResult)

        #Print of the results for player / computer dice rolls
        print("You rolled a " + str(playerResult))
        print("The computer rolled a " + str(computerResult))


        #Decides the winner of the roll
        if playerResult > computerResult and computerScore < 5 and playerScore < 5:
            playerScore = playerScore + 1
            print("You win! You've gained 1 point and now have " + str(playerScore) + " total points. ")
            print("The house has "+ str(computerScore)+ " total points. ")
            input("Press enter to roll: ")
            winner = False

        #If computer rolls higher than the player the computer gets a point
        elif computerResult > playerResult and computerScore < 5 and playerScore < 5:
            computerScore = computerScore + 1
            print("The house wins and has gained 1 point and now has " + str(computerScore) + " total points. ")
            print("You have "+ str(playerScore)+ " total points. ")
            input("Press enter to roll: ")
            winner = False

        #If there's a tie the computer gets a point
        elif computerResult == playerResult and computerScore < 5 and playerScore < 5:
            computerScore = computerScore + 1
            print("It's a tie. 1 point goes to the computer and they now have a total of " + str(computerScore)+ " points. ")
            print("You have "+ str(playerScore)+ " total points. ")
            input("Press enter to roll: ")
            winner = False

#Not necessary for the dice game to run but it adds little ascii dice to make it look nice so i'm leaving it in
def diceDisplay(playerResult):

    if playerResult == 1:
        print(" ")
        print(" -----")
        print("|     |")
        print("|  O  |")
        print("|     |")
        print(" -----")
    
    elif playerResult == 2:
        print(" ")
        print(" -----")
        print("|O    |")
        print("|     |")
        print("|    O|")
        print(" -----")

    elif playerResult == 3:
        print(" ")
        print(" -----")
        print("|O    |")
        print("|  O  |")
        print("|    O|")
        print(" -----")

    elif playerResult == 4:
        print(" ")
        print(" -----")
        print("|O   O|")
        print("|     |")
        print("|O   O|")
        print(" -----")

    elif playerResult == 5:
        print(" ")
        print(" -----")
        print("|O   O|")
        print("|  O  |")
        print("|O   O|")
        print(" -----")

    elif playerResult == 6:
        print(" ")
        print(" -----")
        print("|O   O|")
        print("|O   O|")
        print("|O   O|")
        print(" -----")


def playGameOfSlots(playerName):
  #Available symbols for the slots to choose from
  symbolList = ["Cherry", "Lemon", "Seven", "Diamond", "Heart"]

  playerAttempts = 0
  totalAttempts = 5

  print("Welcome to the casino " + str(playerName) + ". Enjoy the slots. ")

  playerAttemptsUsed = False
  #Loops a slong as the player hasn't tried 5 times or won the game
  while playerAttemptsUsed == False and playerAttempts < 5:
    print("You have used " + str(playerAttempts) + " Attempts")
    input("Press Enter to pull the handle. ")

    resultOne = random.choice(symbolList)
    resultTwo = random.choice(symbolList)
    resultThree = random.choice(symbolList)
    
    print("   [" + str(resultOne)+ "]  ["+str(resultTwo)+ "]   ["+str(resultThree)+ "]   ")

    #Decides if the player wins /loses / ties
    if resultOne == resultTwo and resultTwo == resultThree:
      print("You win! ")
      playerAttemptsUsed = True

    #If player attempts is 5 it sends the player back to the game selection menu
    elif playerAttempts == 5:
      print("You have used up all of your attempts. ")
      playerAttemptsUsed = True

    # Adds to the players attempts until they hit 5
    else:
      playerAttempts = playerAttempts + 1
      remaining = totalAttempts - playerAttempts
      print("You lose. You have " + str(remaining) +" remaining")
      playerAttemptsUsed = False


# This function will return a String containing the new Madlib
def createMadlib(playerName):

    #Text variables
    t1 = "HELP WANTED: Wanted, "
    t2 = " Young Man to work in "
    t3 = " Factory.\n"
    t4 = "Must have "
    t6 = " experience in repairing "
    t7 = " and wrapping "
    t8 = "\n"
    t9 = "Do not apply unless you have "
    t10 = " experience, an I.Q. of at least "
    t11 = "and really enjoy handling "
    #Lists
    adjList = ['weak', 'strong', 'deaf', 'short']
    adjList2 = ['zero', 'no', 'some']
    adjList3 = ['heavy', 'large']
    nounList = ['piano', 'hammer']
    plNounList = ['pianos', 'hammers']
    plNoun2List = ['presents', 'cars']
    numberList = ['1', '50', '100', '150', '200']


    print("Welcome to the casino " + str(playerName) + ". Enjoy some Madlibs. ")

    done = False
    while done == False:
        #Variable to randomly choose a word from each list
        ADJ1 = random.choice(adjList)
        ADJ2 = random.choice(adjList2)
        ADJ3 = random.choice(adjList3)
        NOUN = random.choice(nounList)
        PLNOUN = random.choice(plNounList)
        PLNOUN2 = random.choice(plNoun2List)
        NUMBER = random.choice(numberList)
        
    # Setup the output string that will contain the Madlib
        output = ""

    # Madlib script using concatenation
        output += t1 + str(ADJ1) + t2 + str(NOUN) + t3
        output += t4 + str(ADJ2) + t6 + str(PLNOUN) + t7 + str(PLNOUN2) + t8
        output += t9 + str(ADJ2) + t10 + str(NUMBER) + t8
        output += t11 + str(ADJ3) + " " + str(PLNOUN) + "."

        if done == False:
            done = False
            print(output)
            break
        else:
            done = True
            print("Thanks for playing")
            break
            


#Player Name variable that gives the players name to every function 

playerName = input("Enter your name: ")

selectionMenu(playerName)
