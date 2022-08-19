from tkinter import N


def Name(s):
    hashmap = {}
    n_list = [a for a in s]
    res = []
    print(n_list)
    for i, letter in enumerate(n_list):
        # hashmap[letter] = [i]
        if letter not in hashmap:
            hashmap[letter] = [i]
        else:
            hashmap[letter].append(i)
    print(hashmap)

print(Name('marquita'))

def letterCount(s2):
    hashmap2 = {}
    n_list2 = [b for b in s2]
    for letter in n_list2:
        hashmap2[letter] = n_list2.count(letter)
    print(hashmap2)
print(letterCount('marquita'))