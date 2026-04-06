class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            combined_sum = numbers[l] + numbers[r]

            if combined_sum == target:
                return [l + 1, r + 1]
            elif combined_sum < target:
                l += 1 #i want to make the comibned sum larger by moving up l (the start)
            else:
                r -=1 #smaller when r goes down 1 especially in a sorted list
        