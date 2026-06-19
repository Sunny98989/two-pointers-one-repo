class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if (hour==12):
            h = (hour*0) + minutes * 0.5
        else:
            h = (hour*30) + minutes * 0.5
        mins = minutes*6

        ans = min(abs(mins - h), 360 -  abs(mins - h))

        return ans
