class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:


        hash_set = {}
        counter = 0


        for n in nums:


            if n in hash_set:
                hash_set[n] -= 1
                counter += 1


                if hash_set[n] == 0:
                    del hash_set[n]


            else:
                required_number = k - n
                hash_set[required_number] = hash_set.get(required_number, 0) + 1


        return counter

