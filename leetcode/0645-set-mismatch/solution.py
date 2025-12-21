class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n + 1)

        dup = -1
        missing = -1

        for x in nums:
            freq[x] += 1

        for i in range(1, n + 1):
            if freq[i] == 2:
                dup = i
            elif freq[i] == 0:
                missing = i

        return [dup, missing]

