class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use 2 for loops to solve this problem
        #1 loop for stopping at one index, and another loop for going through all the indicies
        #time: o(n^2), space: o(1)
        #hash map version
        #key value pair
            #key: number
            #value: index
        #target = curr + complement
        #complement = target - curr
        #we can check for the complement based on the curr number in the hash_map
            #if there is a complement based on curr, I return both the index
            #if there is not, I add current to my hash map
        #return the smaller index first, so I will use a conditional if statement

        hash_map = {}

        for curr in range(len(nums)):
            #number (key)
            complement_num = target - nums[curr] 
            if complement_num in hash_map:
                if hash_map[complement_num] < curr:
                    return [hash_map[complement_num], curr]
                else:
                    return [curr, hash_map[complement_num]]
            #if there is no complement, I add the current key and index (pair) to my hashmap
            hash_map[nums[curr]] = curr
        return [] #in case there is no solution
