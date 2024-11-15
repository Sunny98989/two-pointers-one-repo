class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        summ = 0
        res = 0

        for i in gain :
            summ += i
            res = max(res,summ)

        return res


        
