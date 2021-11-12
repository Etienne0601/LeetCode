class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        totalGroups = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        digitsGroups = []
        for s in digits:
            group = totalGroups[int(s) - 2]
            digitsGroups.append(group)
        
        for i in range(len(digitsGroups)):
            
