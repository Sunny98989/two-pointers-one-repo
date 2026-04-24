class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        us = 0
        maxD = 0
        for i in moves:
            if i == "L":
                maxD -= 1
            if i == "R":
                maxD += 1
            if i == "_":
                us += 1
        return max(abs(maxD+us), abs(maxD-us))
