class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we can use 2 pointers solution here
        # lets first find the biggest height
        # and then move the minimum 
        left = 0
        right = len(heights) - 1
        out = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            out = max(area, out)
            if (heights[left] > heights[right]):
                right -= 1
            elif (heights[left] < heights[right]):
                left += 1
            else:
                left += 1
        return out
