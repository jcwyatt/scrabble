#program to give scrabble scores for words


#function to work out the scrabble word score
def wordVal(word,vals): 
    wordVal=0
#   print(word)
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

#define quantities

scrabLetQty={'E':12,'A':9,'I':9,'O':8,'N':6,'R':6,'T':6,'L':4,'S':4,'U':4,
             'D':4, 'G':3,
             'B':2, 'C':2 , 'M':2, 'P':2,
             'F':2,'H':2,'V':2,'W':2,'Y':2,
             'J':1, 'X':1, 'Q':1, 'Z':1
             }
score = 1
while score != 0:

    wordToCheck = str.upper(input("Type in a word, I'll give you it's scrabble score. Press enter to exit.\n"))
    
    score = wordVal(wordToCheck,scrabLetVals)

    print ('score = ', score, '\n')

print('Thanks for using this app!\n')



    
