class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we need to find the sorted half
        # so in that half we can see if we need to 
        # search thru, by checking the value of target
        left = 0
        right = len(nums) - 1 

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # right half is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
