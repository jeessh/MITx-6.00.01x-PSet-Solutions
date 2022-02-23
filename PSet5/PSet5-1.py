class Message(object):
  
    def __init__(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):

        return self.message_text

    def get_valid_words(self):

        return self.valid_words[:]

    def build_shift_dict(self, shift):

        cipherDict = {}
        for charIndex in range(len(string.ascii_lowercase)):
            key = string.ascii_lowercase[charIndex]
            value = string.ascii_lowercase[(charIndex + shift) % 26]
            cipherDict[key] = value
            cipherDict[key.upper()] = value.upper()
        return cipherDict

    def apply_shift(self, shift):
  
        cipherMessageText = ""
        for char in self.message_text:
            if char.isalpha():
                cipherChar = self.build_shift_dict(shift)[char]
            else:
                cipherChar = char
            cipherMessageText += cipherChar
        return cipherMessageText
