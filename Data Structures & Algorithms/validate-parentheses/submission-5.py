class Solution:
    def isValid(self, s: str) -> bool:
        #let say we want to iterate from right to left
        #no problem, we can just change the hash_dict mapping from close to open to open to close
        #instead of pushing the open bracket to the stack, we push the close bracket 
        #instead of popping the open bracket, we pop the close bracket if the close bracket matches the open bracket

        #map the open to close 
        hash_dict = {'(':')', '{':'}', '[':']'}
        stack = []

        for char in reversed(s):
            #will iterate from right to left 
            if char not in hash_dict:
                stack.append(char)
            else:
                if stack and stack[-1] == hash_dict[char]:
                    #if stack != []
                    stack.pop()
                else:
                    return False #return False because the stack is empty 
                    #and there is only close bracket no open bracket leftover
        return not stack #only return True if it empty

        #space: o(n)
        #time: o(n)
