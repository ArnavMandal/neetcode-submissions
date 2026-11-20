class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # ok lets use a set for the seen values,
    # so as long as the current window is not in seen
    # its not duplicate 
        seen = set()

        l = 0
        r = 0
        leng = 0
    
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            leng = max(leng, (r - l + 1))
            r += 1
        return leng