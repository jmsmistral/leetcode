import sys

def romanToInt(s: str) -> int:
    # create map of roman numerals to values
    # iterate through chars in s
    # if char not any valid roman numeral return
    # if char one of I, X, or C, peek at next char in string to see if (V, X), (L, C), or (D, M)
    #   and apply the corresponding subtraction and add to the accumulator
    # else add to the accumulator
    romanToIntMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    exceptionRomanChars = ['I', 'X', 'C']
    ignoreNextChar = False
    sum = 0
    for i in range(len(s)):
        if s[i] not in romanToIntMap.keys():
            return
        if ignoreNextChar:
            ignoreNextChar = False
            continue
        if i != (len(s) - 1) and s[i] in exceptionRomanChars:
            if (s[i] == 'I' and s[i+1] in ('V', 'X') or
               s[i] == 'X' and s[i+1] in ('L', 'C') or
               s[i] == 'C' and s[i+1] in ('D', 'M')):
                sum += (romanToIntMap[s[i+1]] - romanToIntMap[s[i]])
                ignoreNextChar = True
                continue
        sum += romanToIntMap[s[i]]
    return sum



if __name__ == '__main__':
    s = 'III'
    print(romanToInt(s))

    s = 'IV'
    print(romanToInt(s))

    s = 'IX'
    print(romanToInt(s))

    s = 'LVIII'
    print(romanToInt(s))

    s = 'MCMXCIV'
    print(romanToInt(s))
