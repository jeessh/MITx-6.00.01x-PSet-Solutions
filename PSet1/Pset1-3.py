testString = ""
newString = ""

for i in range(len(s)):
    if i == s[0]:
        testString = s[i]
    if s[i] >= s[i-1]:
        testString += s[i]
    elif s[i] < s[i-1]:
        testString = s[i]

    if len(testString) > len(newString):
        newString = testString

print("Longest substring in alphabetical order is: " + newString)
        
