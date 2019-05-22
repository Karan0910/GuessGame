'''
    @author: Karan Sharma
    
    This file is the entry point of the word guessing game

'''
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
    global gameList
    global missedLetters
    global badGuess
    global score
    global lettersCount
    global guessedChars
    if(scorePar>0 and lettersCount>0):
        scorePar=scorePar/lettersCount
    gameList.append({"Game":gameCount,"Word":current_word,"Status":status,"Bad Guesses":badGuessPar,"Missed Letters":missedLettersPar,"Score":scorePar})

    missedLetters=0
    badGuess=0
    score=0
    lettersCount=0
    guessedChars="----"


def guess(real_word):
    """Get the guessed word from user and compare it with real word

    Parameters:
        real_word: Random generated word
        
    """
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
    else:
        print("Try Again!! You guessed a wrong word!!")
        reset=False
        if(score==0):
            score=score-5
        else:    
            score=score-(score*0.10)
        badGuess=badGuess+1
        middleGame=1
    

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
    global score
    gameCount+=1
    score=score-game.calculateWordScore(guessedChars,current_word)
    saveData(gameCount,current_word,"Gave up",badGuess,missedLetters,score)

def letter(real_word):
    """Get the guessed letters from user and compare it with real word

    Parameters:
        real_word: Random generated word
        
    """
    global reset
    global guessedCharCount
    global guessedChars
    global missedLetters
    global gameCount
    global score
    global middleGame
    global lettersCount
    guessedChar = input("Enter an alphabet : ")
    if (guessedChar in real_word):
        checkChar(guessedChar,real_word)

    else:
        print("Try Again!! You guessed a wrong letter")
        missedLetters+=1
        middleGame=1
        lettersCount+=1
    
    if(guessedCharCount==4) :
        gameCount+=1
        reset=True
        middleGame=0
        guessedCharCount = 0 
        guessedChars="----"
        print("Wow! You guessed the word correctly")
        saveData(gameCount,current_word,"Success",badGuess,missedLetters,score)
    else:
        reset=False
        middleGame=1

def quitfx():
    """Quits the current running game

        
    """
    global option
    global middleGame
    global gameCount
    global score
    exitOpt=input("Are you sure you want to quit? y/n: ")
    
    if(exitOpt=="y"):
        if(middleGame==1):
            gameCount+=1
            score=score-game.calculateWordScore(guessedChars,current_word)
            saveData(gameCount,current_word,"Gave up",badGuess,missedLetters,score)
            middleGame=0
        game.printResults(gameList)
        exit()
    else:
        option="c"  





wordArray=stringDatabase.readFile()

if __name__ == '__main__':
    while(option !="q"):
        
        if(reset==True):
            print("**The great guessing game**")
            randomNum=random.randint(1,len(wordArray))
            current_word=wordArray[randomNum]
        print("Current Guess: "+guessedChars)    
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


