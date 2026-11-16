class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        r = 0
        out = 0
        cur = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                cur += 1
                r += 1
            else:
                seen.remove(s[l])
                l += 1
                cur -= 1
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    cur -= 1
            out = max(out, cur)
        return out
                
                

