class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, element in enumerate(nums):
            complement = target - element
            if complement in num_map:
                return [num_map[complement], index]
            num_map[element] = index
        return []

