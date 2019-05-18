def calculateScore(guessedLetter,score):
            frequestLetters="aeiou"
            if(guessedLetter in frequestLetters):
                score=score-2
            else:
                score=score+10

            return score   

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