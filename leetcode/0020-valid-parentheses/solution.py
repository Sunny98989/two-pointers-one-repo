class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        o_b = ["[","{","("]
        valid_stack = []
        for i in range(len(s)):
            if s[i] in o_b:
                valid_stack.append(s[i])
            if s[i] == "]" :
                if len(valid_stack)>0:
                    if valid_stack[-1] == "[":
                        valid_stack.pop()
                    else:
                        return False
                else:
                    return False
            if s[i] == "}":
                if len(valid_stack)>0:
                    if valid_stack[-1] == "{":
                        valid_stack.pop()
                    else:
                        return False
                else:
                    return False
            if s[i] == ")" :
                if len(valid_stack)>0:
                    if valid_stack[-1] == "(":
                        valid_stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if len(valid_stack)>0 else True
