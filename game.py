from stringDatabase import letter_frequency



def calculateScore(guessedLetter,score):
    individualCharscore=score+letter_frequency[guessedLetter]

    return individualCharscore   

def printResults(gameList):
    finalScore=0
    format = "{:<10}{:<10}{:<10}{:<15}{:<15}{:<15}"  
    print (format.format("Game","Word","Status","Bad Guesses","Missed Letters","Score"))
    for row in gameList:
       print (format.format(row['Game'],row['Word'],row['Status'],row['Bad Guesses'],row['Missed Letters'],
       row['Score']))
       finalScore+= row['Score']        
    
    print('\n')
    print("Final Score :"+str(finalScore))

def calculateWordScore(guessedChars,word):
    score=0
    for i in range(len(word)):
        if(word[i]!=guessedChars[i]):
            score=score+letter_frequency[word[i]]

    return score