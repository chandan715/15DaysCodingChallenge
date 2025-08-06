class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        i = 0
        while i < len(s):
            if i > 0 and ((s[i] == ')' and s[i-1] == '(') or
                        (s[i] == ']' and s[i-1] == '[') or
                        (s[i] == '}' and s[i-1] == '{')):
                s.pop(i)
                s.pop(i-1)
                i = i - 2 
                if i < 0:
                    i = 0
            else:
                i += 1
        return len(s) == 0
