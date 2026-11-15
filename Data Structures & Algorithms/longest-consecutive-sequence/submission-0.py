class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # we can start with making the list a set, to remove
    # duplicates and to do O(1) lookup
    # to identify a start of a sequence, we need to see if
    # the number before it isnt in the list
        out = 0
        seen = set(nums)

        for n in seen:
            if n - 1 in seen:
                continue
            else:
            # start of sequence
                cur = 1
                num = n
                while num + 1 in seen:
                    cur += 1
                    num += 1
                out = max(cur, out)
        return out

