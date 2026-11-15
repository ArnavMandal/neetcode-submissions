class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ok lets do this, so we have a target and lets see if 
        # the subtracted number is equal to any number in the nums

        
        out = {}
        ans = []
        for i in range(0, len(nums)):
            if (target - nums[i] in out.keys()):
                ans.append(out[target - nums[i]])
                ans.append(i)
                break
            out[nums[i]] = i            
        return ans
        