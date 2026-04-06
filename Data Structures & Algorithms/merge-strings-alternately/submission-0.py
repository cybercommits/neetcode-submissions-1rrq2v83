class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = ""
        if len(word1) < len(word2):
            longest = len(word2)
        else:
            longest = len(word1)
        for i in range(longest):
            if i < len(word1):
                combined += word1[i]
            if i < len(word2):
                combined += word2[i]
        return combined