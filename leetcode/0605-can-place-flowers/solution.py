class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        extended_flowerbed = [0]+flowerbed+[0]
        for i in range(1,len(flowerbed) + 1):
            if extended_flowerbed[i-1:i+2] == [0,0,0]:
                extended_flowerbed[i] = 1
                n-=1
        return n<=0
        

