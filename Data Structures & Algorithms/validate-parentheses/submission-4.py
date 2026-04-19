class Solution:
    def isValid(self, s: str) -> bool:
        #stack to be declare so I can push the open and pop from it if it matchs
        #hash-map dictionary to map the close to open (to compare)
        #for loop to iterate through the s from left to right 
        #push the open bracket to the stack if it not in the hash-map
        #pop the open if it matches the close
            #stack cannot be empty 
            #the close match the open type hash_map[close] == the top of the stack (open bracket)
        #return true if the stack is empty otherwise return false
        #[[, no close brackets to pop it, then it will be false because the stack is not empty and it is not closed by the same type of bracket
        #brute force: o(n^2) while, delete "[]", which will run the while loop and shift everything back

        hash_dict = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            #will iterate from left to right
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
