class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack:
                if char in (")","]","}"):
                    return False
                else:
                    stack.append(char)
            else:
                if char in (")","}","]"):
                    if stack[-1]=='(' and char == ')' or stack[-1]=='[' and char == ']' or stack[-1]=='{' and char == '}':
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
        if not stack:
            return True
        else:
            return False
                
            
