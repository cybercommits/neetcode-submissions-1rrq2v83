class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I will first create a hash map 
        #key: element value
        #value: element index 
        #target = current (the index in the for loop) + complement
        #complement = target - current 
        #brute force can be o(n^2) time
        #hash map: this can be o(n) time complexity 
        #one pass or two pass
        #for loop to itereate through the nums array
        #one pass will first check if the current has a compliment
            #if it do have a complement, it is going to return both the current and the compliment
            #if it don't, I will just store the key value pair in the hash map so that the next index can find the compliment and check in the hash map
        #if there is no solution, I just return an empty list 
        hash_map = {}

        for i in range(len(nums)):
            complement_value = target - nums[i]
            if complement_value in hash_map:
                #key: element value
                #value: index 
                if i < hash_map[complement_value]:
                    return [i, hash_map[complement_value]]
                else:
                    return [hash_map[complement_value], i]
            #store the current element value and index as key-value pair in my hashmap
            hash_map[nums[i]] = i
        return [] #to ensure that even if there is no solution, this will return an empty list
        #consider edge case
        #o(n) for time
        #o(n) for space 

