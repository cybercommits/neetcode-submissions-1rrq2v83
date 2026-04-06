class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
                #moves the indexes (l up and r down) if it is not alphabet or numerical
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                elif s[l].lower() != s[r].lower():
                    #if not equal, return False automatically
                    return False
                else:
                    #if every thing passes, continue to move the indexes
                    l += 1
                    r -= 1
        return True
