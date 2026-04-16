class Solution:
    def isValid(self, s: str) -> bool:
        #stack to pop the close when the open match, which will iterate
        #from right to left
        #hash_dict to map the open to close
        #for loop (right to left)
        #push the close 
        #pop the close if the stack is not empty and if the close match the open
            #if either stack is empty or the close doesn't match the open:
                #return false because when comparing the open to close, 
                    #it either doesn't have anything to compare with or the match is not correct
                    #example: (( [doesn't have any closed brackets to pop from the stack since it empty, return false]
        #return true if stack is empty

        stack = []
        hash_dict = {'(':')', '{':'}', '[':']'}

        for char in reversed(s):
            if char not in hash_dict: 
                #close brackets push to the stack 
                stack.append(char)
            else:
                if stack and hash_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack 

        #time: o(n), one reversed for loop that will iterate from right to left
        #space: o(n), worst case is pushing n times to the stack to store
