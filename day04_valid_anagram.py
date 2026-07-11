def isAnagram(s, t):

    s = list(s.lower())
    t = list(t.lower())

    if len(s) != len(t):
        return False
    
    counts_s  = {}
    for char in s:
        if char in counts_s:
            counts_s[char] += 1
        else:
            counts_s[char] = 1

    counts_t = {}
    for char in t:
        if char in counts_t:
            counts_t[char] += 1
        else:
            counts_t[char] = 1

    return counts_s == counts_t

print(isAnagram("anagram","nagaram"))
print(isAnagram("car","rat"))


# Another approach for anagram 

# Anagrams

string1 = 'silent'
string2 = 'listen'

string1 = string1.lower()
string2 = string2.lower()

counts = {}
anagram = True

if len(string1) != len(string2):
    anagram = False
    print("Given string is not a anagram")

for char in string1:

    if char in counts:
        counts[char] += 1
    
    else:
        counts[char] = 1

for char in string2:
    
    if char in counts:
        counts[char] -= 1

    else:
        anagram = False
        print("Given strings is not a anagram")
        break

for count in counts.values():
    if count != 0:
        anagram = False

print(anagram)


        

