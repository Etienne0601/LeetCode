class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # if there's only one string, then there can only
        # be one group, so then return that group
        if len(strs) == 1:
            return [strs]
        
        # dictionary that maps letter combinations to list
        # of strings in strs that match that letter combination
        letters = defaultdict(list)
        
        for s in strs:
            # count holds the count of each letter in s
            count = [0] * 26
            for currChar in s:
                count[ord(currChar) - ord("a")] += 1
            # then add s to the letters dictionary
            letters[tuple(count)].append(s)
        
        return letters.values()
