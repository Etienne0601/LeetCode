class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        
        for i in range(1, n+1):
            thisStr = ""
            if i % 3 == 0:
                thisStr += "Fizz"
            if i % 5 == 0:
                thisStr += "Buzz"
            if len(thisStr) == 0:
                thisStr = str(i)
            answer.append(thisStr)
        
        return answer
