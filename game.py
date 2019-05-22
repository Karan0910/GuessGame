from stringDatabase import letter_frequency



def calculateScore(guessedLetter,score):
    """Calculates the score for individual letter

    return: individual letter score        
    """
    individualCharscore=score+letter_frequency[guessedLetter]

    return individualCharscore   

def printResults(gameList):
    """Prints the game result

    Parameters:
        gameList: a list of game result to be printed
        
    """
    finalScore=0
    value_format="{:<10d}{:<10s}{:<10s}{:<15d}{:<15d}{:<15.2f}"
    format = "{:<10}{:<10}{:<10}{:<15}{:<15}{:<15}"  
    print (format.format("Game","Word","Status","Bad Guesses","Missed Letters","Score"))
    print (format.format("-----","-----","------","------------","-------------","-----"))
    for row in gameList:
       print (value_format.format(row['Game'],row['Word'],row['Status'],row['Bad Guesses'],row['Missed Letters'],
       row['Score']))
       finalScore+= row['Score']        
    
    print('\n')
    print("Final Score : {:5.2f}".format(finalScore))

def calculateWordScore(guessedChars,word):
    """Calculate the score of whole word with guessed character

    Parameters:
        guessedChar: a guessed character
        word: randomly generated word
        
    """
    score=0
    for i in range(len(word)):
        if(word[i]!=guessedChars[i]):
            score=score+letter_frequency[word[i]]

    return score