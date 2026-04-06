class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_list = []

        #sort first O(n log n)
        nums.sort()

        #brute force: O(n^3)
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                for z in range(y + 1, len(nums)):
                    target_zero = nums[x] + nums[y] + nums[z]
                    triplet = [nums[x], nums[y], nums[z]]
                    if target_zero == 0 and triplet not in num_list:
                        num_list.append(triplet)
        return num_list