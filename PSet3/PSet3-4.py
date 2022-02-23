def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",str(len(secretWord)),"letters long.")
    print("-------------")

    guessesAvailable = 8
    lettersGuessed = []

    while guessesAvailable > 0:
        print("You have",str(guessesAvailable),"left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        guess = (input("Please guess a letter: ")).lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                guessesAvailable -= 1
        else:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
        print("-------------")
        if isWordGuessed(secretWord,lettersGuessed):
            print("Congratulations, you won!")
            return None

    print("Sorry, you ran out of guesses. The word was else. ")
    return None
