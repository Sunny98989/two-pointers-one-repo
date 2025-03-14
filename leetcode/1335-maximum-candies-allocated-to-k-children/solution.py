class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total<k:
            return 0
        
        l = 1
        r = total//k
        res = 0

        while l<= r:
            mid = (l+r)//2
            count = 0
            for i in candies:
                if i>= mid:
                    count += i//mid
                if count >= k:
                    break
            if count>=k:
                l = mid+1
                res = mid
            else:
                r = mid-1
        return res
            


