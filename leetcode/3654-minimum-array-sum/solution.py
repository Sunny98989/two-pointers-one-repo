class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        INF = 10**20
        N = len(nums)
        @cache
        def go(index, o1, o2):
            if index == N:
                return 0
            best = INF
            # don't use any operations
            r = go(index + 1, o1, o2) + nums[index]
            if r < best:
                best = r
            if o1>0: 
                r = go(index + 1, o1 - 1, o2) + (nums[index] + 1) // 2
                if r < best:
                    best = r
            if o2 > 0:
                
                if nums[index] >= k:
                    r = go(index + 1, o1, o2 - 1) + (nums[index] - k)
                    if r < best:
                        best = r

            if o1> 0 and o2 > 0 and (nums[index] >= k):
                r = go(index + 1, o1 - 1, o2 - 1)
                # subtract first
                sf = (nums[index] - k)
                sf = (sf + 1) // 2
                # divide first
                df = (nums[index] + 1) // 2
                if df >= k:
                    df -= k
                r += min(sf, df)
                if r < best:
                    best = r
            return best
        
        r = go(0, op1, op2)
        go.cache_clear()
        return r

