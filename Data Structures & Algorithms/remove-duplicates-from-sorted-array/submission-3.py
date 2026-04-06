class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = len(nums) - 1
        count = 1

        while r > 0:
            if nums[r] == nums[r - 1]:
                nums.pop(r)
            else:
                count += 1
            r -= 1
        return count
            
        