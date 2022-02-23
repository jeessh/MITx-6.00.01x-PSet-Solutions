def isValidWord(word, hand, wordList):

    new_hand = hand.copy()
    if word in wordList:
        for letter in word:
            try:
                if (letter not in new_hand) or (new_hand.get(letter) == 0):    
                    return False
                else:
                    new_hand[letter] = new_hand.get(letter) - 1
            except KeyError:
                return False
        return True
    else:
        return False 
