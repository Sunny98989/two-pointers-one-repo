class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        for n, cnt in count.items():
            if cnt%2 == 1:
                return False
        return True
