# Let's begin by describing the 6.00 wordgame: This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.

# The rules of the game are as follows:
#
# Dealing
# A player is dealt a hand of n letters chosen at random (assume n=7 for now).
#
# The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
#
# Some letters may remain unused (these won't be scored).
#
# Scoring
# The score for the hand is the sum of the scores for each word formed.
#
# The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
#
# Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.
#
# For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
#
# As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    newrandomhand = {}
    ucFlag = ""
    userINPUT = input(
        "Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")

    while userINPUT not in ('n', 'r', 'e'):
        userINPUT = input("Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")

    while userINPUT != 'e':
        if userINPUT == 'n':
            ucFlag= input("Enter u to have yourself play, c to have the computer play:")
            if ucFlag == 'u':
                newrandomhand = dealHand(HAND_SIZE)
                playHand(newrandomhand, wordList, calculateHandlen(newrandomhand))
                userINPUT = input("Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")

            elif ucFlag == 'c':
                newrandomhand = dealHand(HAND_SIZE)
                compPlayHand(newrandomhand, wordList, calculateHandlen(newrandomhand))
                userINPUT = input("Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")

            else:
                while ucFlag not in "uc":
                    print("Invalid command.")
                    ucFlag = input("Enter u to have yourself play, c to have the computer play:")

        elif userINPUT == 'r':
            if not newrandomhand:
                print("You have not played a hand yet. Please play a new hand first!")
                userINPUT = input("Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")
                if userINPUT == 'e':
                    break

            elif newrandomhand:
                ucFlag = input("Enter u to have yourself play, c to have the computer play:")
                if ucFlag == 'u':
                    newrandomhand = dealHand(HAND_SIZE)
                    playHand(newrandomhand, wordList, calculateHandlen(newrandomhand))
                    userINPUT = input("Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")

                elif ucFlag == 'c':
                    newrandomhand = dealHand(HAND_SIZE)
                    compPlayHand(newrandomhand, wordList, calculateHandlen(newrandomhand))
                    userINPUT = input("Please enter 'n' to play a new random hand, 'r' to play the last hand again or e to exit the game. ")

                else:
                    while ucFlag not in "uc":
                        print("Invalid command.")
                        ucFlag = input("Enter u to have yourself play, c to have the computer play:")



        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


