class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        braces = {'[': ']', '{': '}', '(': ')'}

        for i in s:
            if i == '[' or i  == '{' or i == '(':
                stk.append(i)
            else:
                if len(stk) > 0 and i == braces[stk[-1]]:
                    stk.pop()
                else:
                    return False
        if len(stk) != 0:
            return False
        return True
            
             