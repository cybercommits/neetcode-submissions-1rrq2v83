class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in map:
                #creates the empty list first
                map[key] = [] 
            #after creating the empty list, i can safetly append
            map[key].append(word)
        return list(map.values())
            
            
