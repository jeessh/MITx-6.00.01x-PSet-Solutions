def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
# FILL IN YOUR CODE HERE...

    availableLetters = ''
    for alphabet in string.ascii_lowercase:
        if alphabet not in lettersGuessed:
            availableLetters += alphabet
    return availableLetters
