class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        Candies_list = []
        for i in candies:
            if i + extraCandies >= maxCandies:
                Candies_list.append(True)
            else:
                Candies_list.append(False)
        return Candies_list

