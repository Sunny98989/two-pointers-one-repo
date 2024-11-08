class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = sorted(nums1+nums2)
        length_of_total = i = len(total)

        if length_of_total %2 == 0:
            return (total[i//2] + total[(i//2)-1])/2
        else:
            return total[i//2]
