class Solution:
    def isValid(self, s: str) -> bool:
        #hash map dictoinary to map the open to the close bracket
            #open:close, iterate the loop from right to left 
            #close:open, iterating the loop from left to right
        #stack 
        #loop that will go from right to left 
            #if the open bracket is inside the hash_map:
                #pop the closed bracket if the open bracket match, same type 
                    #make sure the stack is not empty 
                    #make sure that the open bracket match the close bracket
                    #if any of these two conditions above fails, then it is false 
            #else: 
                #push the closed bracket to the stack, I will have to start from right to left
        #return True if stack is empty, otherwise I will have to return False 
        #brute force: a while loop with a replace function that replaces the matching open to close bracket type
        #allocate new memory string, space O(N)
        #time: o(n^2)
        stack = []
        #maps the open to the close 
        hash_dict = {'(':')', '{':'}', '[':']'}

        #loop to iterate from right to left, so I can push the closed brackets
        for i in range(len(s) - 1, -1, -1):
            if s[i] in hash_dict:
                if stack and hash_dict[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack == []:
            return True
        else:
            return False
        #return true if the stack is empty, otherwise return false if the stack is not empty


