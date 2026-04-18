class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #no two pointers since nums is not sorted
        #i will use a hash map to solve this where I can store the key value pairs
        #and find the compliment 
        #target = current + compliment
        #compliment = target - current 
        #if you find the compliment in the hash map, you can return the current index
        #and the compliment, hence finding the target

        hash_map = {}

        #one pass where we first check if there is a compliment from the current value 
        #to add up to target
        #if there is no compliment found, we can store the current key value pair in the hash_map and move up one

        for i in range(len(nums)):
            #key: element value
            #value: element index 
            compliment_value = target - nums[i]
            #this has to be nums[i], which is the element value
            if compliment_value in hash_map:
                if hash_map[compliment_value] < i:
                    return [hash_map[compliment_value], i]
                else:
                    return [i, hash_map[compliment_value]]
            #not in hash_map, store as key value pairs:
            hash_map[nums[i]] = i
        return [] #if there is no solution, but in this problem there is exactly one pair that satisfy

        #time: o(n)
        #space: o(n)