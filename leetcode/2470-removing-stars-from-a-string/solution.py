class Solution:
    def removeStars(self, s: str) -> str:
        ret_str = ""

        for idx,s in enumerate(s):
            if s == "*":
                ret_str = ret_str[:-1]
            else:
                ret_str = ret_str+s

        return ret_str
