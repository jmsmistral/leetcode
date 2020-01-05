import sys
from collections import defaultdict


def groupAnagrams(strs):
    # Order each string in array
    # Order array by string
    # Iterate through array, and process groups starting with the same letter
        # function should return groups
    anagramMap = defaultdict(list) # anagram + list of indices
    for i in range(len(strs)):
        val = ''.join(sorted(strs[i]))
        anagramMap[val].append(strs[i])
    return [anagramMap[group] for group in anagramMap]

if __name__ == '__main__':
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(a))
    # Expected output:
    # [
    #     ["ate","eat","tea"],
    #     ["nat","tan"],
    #     ["bat"]
    # ]
