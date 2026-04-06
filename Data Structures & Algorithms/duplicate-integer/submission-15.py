class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #creates an empty hashset
        seen = set()

        #loop through all the integers in nums
        for integer in nums:
            #if there is an integer n in seen, you return true
            if integer in seen:
                return True
            #if this is new and never seen, you add integer in seen
            seen.add(integer)
        #after loop runs, return False if there is no duplicate (no True)
        return False
        