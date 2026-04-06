class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = ""
        shortest_length = min(len(word) for word in strs)

        for i in range(shortest_length):
            comparison = strs[0][i]
            
            for word in strs[1:]: #takes only index 1 of strs and goes to the end
                if comparison != word[i]: #compare the chars to see if it the same, if not return
                    return prefix
            prefix += comparison #adds the comparison to the prfix 
        return prefix