class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 <stack[-1]:
                if abs(a) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a) == stack[-1]:
                    stack.pop()
                    a = 0
                break
            else:
                stack.append(a)
        return stack
