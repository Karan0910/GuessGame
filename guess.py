import os
import random
import game
import stringDatabase
from stringDatabase import letter_frequency

reset=True
guessedCharCount=0
guessedChars="----"
score=0
gameCount=0
badGuess=0
missedLetters=0
middleGame=1
gameList = []
option = 'n'
lettersCount=0

# define the function blocks
def saveData(gameCount,current_word,status,badGuessPar,missedLettersPar,scorePar):
    """Gets and save the game's data into the list

    Parameters:
        gameCount: number of games played
        current_word : Current word played on the game
        status: Set the status to Success if correct word is guessed else Gave up
        badGuessPar: Number of bad guesses made
        missedLettersPar: Number of right letters missed
        scorePar: Score for the current game
    """
    # Get a dictionary 
    global gameList
    global missedLetters
    global badGuess
    global score
    global lettersCount
    if(scorePar>0):
        scorePar=scorePar/lettersCount
    gameList.append({"Game":gameCount,"Word":current_word,"Status":status,"Bad Guesses":badGuessPar,"Missed Letters":missedLettersPar,"Score":scorePar})

    missedLetters=0
    badGuess=0
    score=0
    lettersCount=0


def guess(real_word):
    """Get the guessed word from user and compare it with real word

    Parameters:
        real_word: Random generated word
        
    """
    print ("You typed guess.\n")
    global reset
    global badGuess
    global gameCount
    global score
    global middleGame
    guessed_word = input("Enter the word : ")
    if (real_word==guessed_word):
        print("Woo Hoo, You are absolutely right")
        reset=True
        gameCount+=1
        middleGame=0
        score=score+game.calculateWordScore(guessedChars,current_word)
        saveData(gameCount,current_word,"Success",badGuess,missedLetters,score)
        print("here in true")
    else:
        print("Try Again!!")
        reset=False
        score=score-(score*0.10)
        badGuess=badGuess+1
        middleGame=1
        print("here in false")
    

def checkChar(guessedChar,real_word):
    """Check's if guessed letter is in the generated word

    Parameters:
        guessedChar: letter guessed by user
        real_word: Random generated word
        
    """
    global reset
    global guessedCharCount
    global guessedChars
    global score
    global lettersCount
    for i in range(len(real_word)):
        if(real_word[i]==guessedChar):
            guessedCharCount=guessedCharCount+1
            index=i
            guessedChars=list(guessedChars)
            guessedChars[index]=guessedChar
            guessedChars="".join(guessedChars)
            lettersCount+=1
            score=game.calculateScore(guessedChar,score)


            


def tell(real_word):
    """Prints the real word when user gives up

    Parameters:
        real_word: Random generated word
        
    """
    print ("You gave up!!\n")
    print("Correct word is : "+current_word)
    global gameCount
    gameCount+=1
    saveData(gameCount,current_word,"Gave up",badGuess,missedLetters,score)

def letter(real_word):
    """Get the guessed letters from user and compare it with real word

    Parameters:
        real_word: Random generated word
        
    """
    print ("letter\n")
    global reset
    global guessedCharCount
    global guessedChars
    global missedLetters
    global gameCount
    global score
    global middleGame
    global lettersCount
    guessedChar = input("Enter and alphabet : ")
    if (guessedChar in real_word):
        
        checkChar(guessedChar,real_word)
        print("You gussed "+str(guessedCharCount)+" letters")
        print(score)

    else:
        print("Try Again!!")
        missedLetters+=1
        #score=score-game.calculateScore(guessedChar,score)
        middleGame=1
        lettersCount+=1
    
    print("asdafasdfasdfadfasdfadsfasdfadsfaf"+str(guessedCharCount))
    if(guessedCharCount==4) :
        gameCount+=1
        reset=True
        middleGame=0
        guessedCharCount = 0 
        guessedChars="----"
        saveData(gameCount,current_word,"Success",badGuess,missedLetters,score)
    else:
        reset=False

def quitfx():
    """Quits the current running game

        
    """
    global option
    global middleGame
    global gameCount
    global score
    print ("quit\n")
    print("asdfasf")
    exitOpt=input("Are you sure you want to quit? y/n: ")
    
    if(exitOpt=="y"):
        if(middleGame==1):
            gameCount+=1
            score=score-game.calculateWordScore(guessedChars,current_word)
            saveData(gameCount,current_word,"Gave up",badGuess,missedLetters,score)
            middleGame=0
        print("data")
        game.printResults(gameList)
        exit()
    else:
        option="c"  


print("**The great guessing game**")

      
wordArray=stringDatabase.readFile()

print(len(wordArray))
while(option !="q"):
    
    if(reset==True):
        randomNum=random.randint(1,len(wordArray))
        current_word=wordArray[randomNum]
        #current_word="abcd"
    
    print("Current Guess: "+guessedChars)    
    print("Curent word:"+wordArray[randomNum])
    print("g = guess, t = tell me, l for a letter, and q to quit")
    option = input() 
    if(option=='g'):
       guess(current_word)
    elif(option=='t'):
       tell(current_word)
    elif(option=='l'):
       letter(current_word)
    elif(option=='q'):
       quitfx()
    else:
       print("Enter correct option!!")


