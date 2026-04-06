class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case if length is not same, return false automatically
        if len(s) != len(t):
            return False

        #two hash tables
        map_s = {}
        map_t = {}

        #fill the hash tables with values
        for char in s:
            if char in map_s:
                map_s[char] += 1
            else:
                map_s[char] = 1
        for char in t:
            if char in map_t:
                map_t[char] += 1
            else:
                map_t[char] = 1
        for char in map_t:
            if map_s.get(char, 0) != map_t[char]:
                return False
        return True

