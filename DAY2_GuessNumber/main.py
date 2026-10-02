import random

def hint1(gtn , guessHistory : int):
    choice = random.randint(1,3)
    if choice == 1:
        if gtn %2 == 0 and gtn != 0:
            return "The Number is an Even Integer."
        elif gtn %2 != 0 and gtn != 0:
            return "The Number is an Odd Integer."
        else:
            return "Dividing this number by itself is not defined."
    elif choice == 2:
        if gtn > 50:
            return "The number is Above 50."
        else:
            return "The number is Below 50."
    elif choice == 3:
        guessHistory.sort()
        l , r = 0 , len(guessHistory)-1
        while l < r:
            mid = (l+r)//2
            if guessHistory[mid] > gtn and guessHistory[mid-1] < gtn:
                return "The number is between" , guessHistory[mid-1] , "to" , guessHistory[mid]
            elif guessHistory[mid] > gtn and guessHistory[mid-1] > gtn:
                r = mid
            else:
                l = mid+1
                
def tooHigh(guess,gtn : int) -> bool:
    if guess > gtn:
        return True
    else : 
        return False

def tooLow(guess,gtn : int) -> bool:
    if guess < gtn:
        return True
    else:
        return False

def ruleBook() -> str:
    return "Rules-\n1. Choose an integer x , where x is the maximum number possible in the round(ideally , 50+)\n2.Choose the number of tries\n3.Guess a number from 1-x\n4.You get a message if the guessed nnumber is higher/lower than the number to be guessed.\n5.You may use upto 3 hints , each hint costs 1 extra try , so you lose 2 tries instead of 1 in the round in which you took hint.\nGood Luck!"

cont = True
while cont:
    print("=+=+ Guess The Number +=+=")
    choice = int(input("Choose one option :\n1.Play\n2.Rules\n3.Exit\nChoice(1/2/3) : "))
    if choice == 1:
        hintHistory = []
        guessHistory = []
        hints = 3
        print("Welcome to the Game!")
        diff = int(input("Enter the maximum INTEGER to guess from(press 0 for rulebook) : "))
        if diff != 0:
            gtn = random.randint(1 , abs(diff))
        else:
            print(ruleBook())
            continue
        tries = int(input("How many tries do you want? : "))
        n = tries
        while abs(tries):

            print("OkiDoki " , abs(tries) , " tries left.")
            print("+-+-+-+- Lets Start Guessing! -+-+-+-+")
            guess = int(input("Guess a number: "))
            guessHistory.append(guess)
            
            if tooHigh(guess , gtn):
                print("Your guessed number is High , try to guess a lower number!")
            elif tooLow(guess , gtn):
                print("Your guessed number is Low , try to guess a higher number!")
            else:
                print("WooHoo!You guessed the right number in " , (n-tries) , " tries.")
                break
            if hints != 0:

                takeHint = input(("Do you want to take a hint(y/n)?(Taking hint Consumes 1 extra try.) : "))
                hintIncomplete = True
                while hintIncomplete:
                    if takeHint == 'y' or takeHint == 'yes':
                        hint = hint1(gtn , guessHistory)
                        if hint in hintHistory:
                            continue
                        else:
                            print(hint)
                            tries -= 1
                            hints -= 1
                            hintIncomplete = False
                            hintHistory.append(hint)

            else:
                print("Hints are finished.")
            tries -= 1

    elif choice == 2:
        print(ruleBook())

    elif choice == 3:
        print("Sayonara ~")
        cont = False