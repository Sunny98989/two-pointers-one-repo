class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = r = 1
        product = [1]*len(nums)

        for i in range(len(nums)):
            product[i] *= l
            l *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            product[i]*=r
            r *= nums[i]

        return product
