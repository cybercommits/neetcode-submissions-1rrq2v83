class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_list = []

        #sort first O(n log n)
        nums.sort()

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            left = x + 1
            right = len(nums) - 1
            while left < right: 
                total = nums[x] + nums[left] + nums[right]
                triplet = [nums[x], nums[left], nums[right]]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    num_list.append(triplet)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return num_list