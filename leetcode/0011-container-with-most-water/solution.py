class Solution:
    def maxArea(self, height: List[int]) -> int:

        first_pointer = 0
        last_pointer = -1
        answer =  0
        lenght = len(height)-1

        while first_pointer != (lenght + last_pointer + 1):
            
            limit = min(height[first_pointer], height[last_pointer])
            dist_x = first_pointer
            dist_y = lenght + last_pointer + 1
            total_dist = dist_y - dist_x
            area = total_dist * limit
            
            if height[first_pointer] > height[last_pointer]:
                last_pointer -= 1
            else:
                first_pointer += 1
            if area > answer:
                answer = area

        return answer


