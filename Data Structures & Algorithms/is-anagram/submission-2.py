class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()

        if len(s) != len(t):
            return False
        
        l = 0
        while l < len(s_list):
            if s_list[l] != t_list[l]:
                return False
            else:
                l += 1
        return True