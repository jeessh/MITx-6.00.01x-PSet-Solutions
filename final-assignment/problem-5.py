"""
Implement a function that meets the specifications below.

def cipher(map_from, map_to, code):
    ''' map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. 
        '''
    # Your code here
For example,

cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    
    parseDict = {}
    tempLetter = ''
    newCode = ''
    
    for i in range(len(map_from)):
        map1 = map_from[i]
        map2 = map_to[i]
        parseDict[map1] = map2
        
    for i in range(len(code)):
        if code[i] in parseDict.keys():
            tempLetter = parseDict.get(code[i])
            newCode = newCode + tempLetter
    
    cipherCode = (parseDict, newCode)
        
    return cipherCode


cipher("abcd", "dcba", "dab")
