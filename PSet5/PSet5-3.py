class CiphertextMessage(Message):
    def __init__(self, text):

        Message.__init__(self, text)

    def decrypt_message(self):

        word_list = load_words(WORDLIST_FILENAME)

        max_count = 0
        decryptedText = ''
        bestShift = None

        for s in range(1, 27):
            text = self.apply_shift(26 - s)
            textList = text.split(' ')
            count = 0
            for word in textList:
                if is_word(word_list, word):
                    count += 1
            if count > max_count:
                max_count = count
                bestShift = 26 - s
                decryptedText = text
        return (bestShift, decryptedText)
