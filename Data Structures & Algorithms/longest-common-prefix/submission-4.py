class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        shortest_length = len(strs[0])
        prefix = ""
        count = 0

        #find the shortest length in the strs list
        #o(n) 
        for i in range(1, len(strs)):
            if len(strs[i]) < shortest_length:
                shortest_length = len(strs[i])

        while count < shortest_length:
            #o(n-1)
            for n in range(len(strs) - 1):
                if strs[n][count] != strs[n+1][count]:
                    return prefix
            prefix += strs[0][count]
            count += 1
        return prefix