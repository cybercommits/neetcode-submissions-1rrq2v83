class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = ""
        shortest_length = min(len(s) for s in strs)

        for i in range(shortest_length):
            comparison = strs[0][i]
            
            for s in strs[1:]:
                if comparison != s[i]:
                    return prefix
            prefix += comparison
        return prefix