class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case if length is not same, return false automatically
        if len(s) != len(t):
            return False
        map = {}

        #fill the map with values 
        for char in s:
            #add for s 
            map[char]= map.get(char, 0) + 1 
        for char in t:
            #subtract for t
            map[char]= map.get(char, 0) - 1
        for char in map:
            if map.get(char, 0) != 0:
                return False
        return True

