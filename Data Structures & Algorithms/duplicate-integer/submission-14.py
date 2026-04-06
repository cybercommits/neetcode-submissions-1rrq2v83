class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for integer in nums:
            map[integer] = map.get(integer, 0) + 1
        
        for integer in map:
            if map[integer] >= 2:
                return True
        return False