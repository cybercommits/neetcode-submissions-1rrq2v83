class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        s1 = min(strs)
        s2 = max(strs)

        char_list = []

        for i in range(len(s1)):
            if i >= len(s2) or s1[i] != s2[i]:
                break
            char_list.append(s1[i])
        return "".join(char_list)
