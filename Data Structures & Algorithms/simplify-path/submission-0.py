class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        # lets use a stack, push the valid dir names
        # pop if we get .. and ignore if .
        # lets split so we can get all dirs
        for ch in path.split('/'):
            if ch == '.' or ch == "":
                continue
            elif ch == '..':
                if len(stk) != 0:
                    stk.pop()
            else:
                stk.append(ch)
        return "/" + '/'.join(stk)

                
            