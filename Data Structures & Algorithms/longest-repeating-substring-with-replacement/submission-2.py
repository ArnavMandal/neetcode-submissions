class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l = 0
        r = 0
        counts = defaultdict(int)
        leng = 0
        while r < len(s):
            counts[s[r]] += 1
            isValid = (r - l + 1) - max(counts.values()) <= k
            while not isValid:
                counts[s[l]] -= 1
                l+=1
                isValid = (r - l + 1) - max(counts.values()) <= k
            leng = max(leng, r - l + 1)
            r += 1
        return leng
