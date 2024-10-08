# 13. Roman to Integer

def convert(s):
    map = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    res = 0
    for i in range(len(s)):
        if i < len(s) - 1 and map[s[i]] < map[s[i+1]]:
            res -= map[s[i]]
        else:
            res += map[s[i]]
    return res