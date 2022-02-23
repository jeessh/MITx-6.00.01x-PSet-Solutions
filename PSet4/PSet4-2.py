def updateHand(hand, word):

    new_hand = hand.copy()
    for letter in word:
        new_hand[letter] = new_hand.get(letter) - 1
    return new_hand
