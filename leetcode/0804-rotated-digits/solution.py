class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_count = 0
        
        for i in range(1, n + 1):
            s = str(i)
            # If it has any invalid digits, skip it entirely
            if '3' in s or '4' in s or '7' in s:
                continue
            
            # If it survived, does it have at least one flipper?
            if '2' in s or '5' in s or '6' in s or '9' in s:
                good_count += 1
                
        return good_count
