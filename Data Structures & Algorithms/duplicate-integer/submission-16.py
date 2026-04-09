class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Hashmap 
        #iterate through the nums array 
        seen = set()

        for element in nums:
            if element in seen:
                return True
            #not in seen, add it
            seen.add(element)
        return False