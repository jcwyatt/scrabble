#program to give scrabble scores for words


#function to work out the scrabble word score

def wordVal(word,vals): 
    wordVal=0
    for letter in word:
        if letter in vals:
            wordVal = wordVal + vals[letter]
        else:
            return ('error - must be letters')
    return(wordVal)    



#define letter values

scrabLetVals={}
for i in ('E','A','I','O','N','R','T','L','S','U'):
    scrabLetVals[i] = 1
for i in ('D','G'):
    scrabLetVals[i] = 2
for i in ('B','C','M','P'):
    scrabLetVals[i] = 3
for i in ('F','H','V','W','Y'):
    scrabLetVals[i] = 4
for i in ('K'):
    scrabLetVals[i] = 5
for i in ('J','X'):
    scrabLetVals[i] = 8
for i in ('Q','Z'):
    scrabLetVals[i] = 10



#define tile quantities

scrabLetQty={'E':12,'A':9,'I':9,'O':8,'N':6,'R':6,'T':6,'L':4,'S':4,'U':4,
             'D':4, 'G':3,
             'B':2, 'C':2, 'M':2, 'P':2,
             'F':2, 'H':2, 'V':2, 'W':2, 'Y':2,
             'K':1, 'J':1, 'X':1, 'Q':1, 'Z':1
             }

#main program

score = 1                    #initialise score to non zero amount


while score != 0:

    status = 'ok'            # initialise status of validity of word

    wordToCheck = str.upper(input("Type in a word, I'll give you it's scrabble score. Press enter to exit.\n"))


#is it valid (number of tiles in the bag)
    for letter in scrabLetQty:
        if wordToCheck.count(letter)>scrabLetQty[letter]:
            print('You used letter %s too many times, there are only %s of those tiles\n' % (letter, scrabLetQty[letter]))
            status = 'void'

#is it long enough (4 letter word or more)
    if  0 < len(wordToCheck) < 4 :
        print('Words must be 4 or more characters\n')
        status = 'void'


    if status != 'void':
        score = wordVal(wordToCheck,scrabLetVals)
        print ('score = ', score, '\n')


#if no word entered, exit the program
        
print('Thanks for using this app!\n')

    
