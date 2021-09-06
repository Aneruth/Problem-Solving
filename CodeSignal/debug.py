# Method 1
def goodBad(s):
    vowels = ["a", "e", "i", "o", "u"]
    counter,alphaCount = 0,0    
    if len(s) == 1 or s == '?': return 'good' or 'bad'
    if s.isalpha() == False: return 'Mixed'
    for i in s:
        if i in vowels or i.isalpha() == False:
            counter += 1
            alphaCount += 1
            if counter >= 3 or counter >= 5 or alphaCount >2:
                return 'bad'
    return 'good'

print(goodBad("qwrtl"))