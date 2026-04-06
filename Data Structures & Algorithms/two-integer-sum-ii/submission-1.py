class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #set two integers, one equal to the start and the other equal to the end
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r +1]
            elif current_sum < target:
                l += 1 #make the sum larger by moving l up and r stays
            else:
                r -= 1 #make the sum smaller by moving r down and l stays