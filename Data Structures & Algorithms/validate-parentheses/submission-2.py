class Solution:
    def isValid(self, s: str) -> bool:
        #hash_map dictionary to map the open to the close
        #Instead of me going from left to right, I go right to left
        #i will use a stack so I can push/pop the closed brackets
        #i use a for loop to iterate through the loop once
            #will go right to left
            #push the close bracket to the stack, I will need to see if it is close bracket
            #pop the close bracket if the open bracket matches
                #if the open bracket don't match, I return False
                #if the stack is empty, I return false
                #because I am comparing open to close
                #if the stack don't have the close while comparing open, then it is false
            #after the for loop is finished, I will check if the stack is empty or not
            #if the stack is empty, return True 
            #otherwise, return False ex: [[

        stack = []
        hash_dict = {'(':')', '{':'}', '[':']'}

        #iterating from the end to the start (right to left)
        for char in reversed(s):
            if char not in hash_dict:
                stack.append(char)
            else:
                if stack and hash_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack
        #time: o(N)
        #space: o(N)