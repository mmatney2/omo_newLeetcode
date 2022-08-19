def anagram(s, t):
    hashMap = {}
    hashMap2 = {}
    if len(s) != len(t):
        return False
    for letter in s:
        if letter not in hashMap:
            hashMap[letter] = s.count(letter)
            print(hashMap)
    for letters in t:
        if letters not in hashMap2:
            hashMap2[letters] = t.count(letters)
            print(hashMap2)
    if hashMap == hashMap2:
        return True
    return False

print(anagram('anagram', 'nagaram'))

