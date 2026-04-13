class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        r,l=-1,-1
        for i in range(start,len(nums)):
            if nums[i] == target:
                r = abs(i - start)    
                break
        for i in range(start, -1, -1):
            if nums[i] == target:
                l = abs(i - start)
                break
        if r != -1 and l != -1:
            return min(r, l)
        if r != -1:
            return r
        return l
        

