class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dynamic
        indexed_nums = []
        #i is the index
        #n is the value
        #in two sum, we swap the index and value so we look for the value first then return the index based on the value
        for i, n in enumerate(nums):
            indexed_nums.append((n, i))
        #sort
        indexed_nums.sort()

        l, r = 0, len(indexed_nums) - 1
        
        while l < r:
            combined_sum = indexed_nums[l][0] + indexed_nums[r][0]

            if target == combined_sum:
                if indexed_nums[l][1] < indexed_nums[r][1]:
                    return[indexed_nums[l][1], indexed_nums[r][1]]
                else:
                    return[indexed_nums[r][1], indexed_nums[l][1]]
            elif combined_sum < target:
                l += 1
            else:
                r -=1