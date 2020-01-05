def lengthOfLongestSubstring(s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        maxSubLen = 1
        currentLen = 0
        currentSub = set()

        for i in range(len(s)):
            currentSub = set(s[i])
            currentLen = 1
            for char in s[i + 1:]:
                if char in currentSub:
                    break
                currentSub.add(char)
                currentLen += 1
                maxSubLen = max(maxSubLen, currentLen)
        return maxSubLen


if __name__ == '__main__':
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))

    s = ' '
    print(lengthOfLongestSubstring(s))

    s = 'au'
    print(lengthOfLongestSubstring(s))

    s = 'dvdf'
    print(lengthOfLongestSubstring(s))
