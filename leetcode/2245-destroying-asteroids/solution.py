import math


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        buckets = [[math.inf, 0] for _ in range(18)]
        for a in asteroids:
            tier = a.bit_length() 
            
            if a < buckets[tier][0]:
                buckets[tier][0] = a
                
            buckets[tier][1] += a
            
        for min_val, total_sum in buckets:
            if total_sum == 0:
                continue
                
            if mass < min_val:
                return False
                
            mass += total_sum
            
        return True
