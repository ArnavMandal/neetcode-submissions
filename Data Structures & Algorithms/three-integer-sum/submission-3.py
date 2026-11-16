class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        # ok we can use like a 2 pointers technique for this, 
        # iterate thru the list with i and then ptr left, 
        # ptr right are what we need to change to reach 0
        # so we keep changing the ptr till we reach 0

        # we need to consider duplicates
        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur < 0:
                    # too negative so we move
                    left += 1
                if cur > 0:
                    # too positive so we move
                    right -= 1
                if cur == 0:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                    
                    
            
        return out
                


