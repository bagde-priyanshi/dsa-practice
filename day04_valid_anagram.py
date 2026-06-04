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