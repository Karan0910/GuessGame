import os
import random
import game

reset=True
guessedCharCount=0
guessedChars="----"
score=0
gameCount=0
badGuess=0
missedLetters=0

myList = []

# define the function blocks

def saveData(gameCount,current_word,status,badGuessPar,missedLettersPar,scorePar):
    # Get a dictionary 
    global myList
    global missedLetters
    global badGuess
    global score
    myList.append({"Game":gameCount,"Word":current_word,"Status":status,"Bad Guesses":badGuessPar,"Missed Letters":missedLettersPar,"Score":scorePar})

    missedLetters=0
    badGuess=0
    score=0


def guess(real_word):
    print ("You typed guess.\n")
    global reset
    global badGuess
    global missedLetters
    global gameCount
    global score
    guessed_word = input("Enter the word : ")
    if (real_word==guessed_word):
        print("Woo Hoo, You are absolutely right")
        reset=True
        gameCount+=1
        score=score+20
        saveData(gameCount,current_word,"Success",badGuess,missedLetters,score)
        print("here in true")
    else:
        print("Try Again!!")
        reset=False
        score=score-20
        missedLetters+=4
        badGuess=badGuess+1
        print("here in false")
    

def checkMultipleChar(guessedChar,real_word):
    global reset
    global guessedCharCount
    global guessedChars
    global score
    for i in range(len(real_word)):
        if(real_word[i]==guessedChar):
            guessedCharCount=guessedCharCount+1
            index=i
            guessedChars=list(guessedChars)
            guessedChars[index]=guessedChar
            guessedChars="".join(guessedChars)
            score=score+10


            


def tell(real_word):
    print ("You gave up!!\n")
    print("Correct word is : "+current_word)
    global gameCount
    gameCount+=1
    saveData(gameCount,current_word,"Gave up",badGuess,missedLetters,score)

def letter(real_word):
    print ("letter\n")
    global reset
    global guessedCharCount
    global guessedChars
    global missedLetters
    global gameCount
    global score
    guessedChar = input("Enter and alphabet : ")
    if (guessedChar in real_word):
        
        characterCount=real_word.count(guessedChar)
        checkMultipleChar(guessedChar,real_word)
        

        print("You guessed "+str(guessedCharCount)+" letters")
    else:
        print("Try Again!!")
        missedLetters+=1
        score=score-5
    if(guessedCharCount==4) :
        gameCount+=1
        reset=True
        guessedCharCount = 0 
        guessedChars="----"
        saveData(gameCount,current_word,"Success",badGuess,missedLetters,score)
    else:
        reset=False

def quitfx():
    print ("quit\n")
    format = "{:<10}{:<10}{:<10}{:<15}{:<15}{:<15}"    
    print (format.format("Game","Word","Status","Bad Guesses","Missed Letters","Score"))
    for row in myList:
       print (format.format(row['Game'],row['Word'],row['Status'],row['Bad Guesses'],row['Missed Letters'],
       row['Score']))  


print("**The great guessing game**")
option = 'n'
# text_file = open("four_letters.txt", "r")
# line = text_file.read().split(' ')

# length=len(line)
# print(length)

list_of_lists = []
word_array=[]
length=0
with open("four_letters.txt", "r") as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(' ')]
        for i in range(len(inner_list)):
            word_array.append(inner_list[i])
        
        list_of_lists.append(inner_list)
        length=length+len(inner_list)
        


print(len(word_array))
while(option !="q"):
    
    if(reset==True):
        randomNum=random.randint(1,length)
        current_word=word_array[randomNum]
        #current_word="oaoo"
        
    
    print("Current Guess: "+guessedChars)    
    print("Curent word:"+word_array[randomNum])
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
    #menu_options(option,current_word)  