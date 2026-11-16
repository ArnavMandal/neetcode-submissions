class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we need to use sliding window,
        # we start with left = 0, and right = 1
        # calculate the difference, and if you find
        # an invalid condition (like a new min)
        # lets set min to that
        if (len(prices) == 1):
            return 0
        l = 0
        r = 1
        out = 0
        while r < len(prices):
            out = max(out, prices[r] - prices[l])
            if prices[r] < prices[l]:
                # new min
                l = r
            r += 1
        return out
