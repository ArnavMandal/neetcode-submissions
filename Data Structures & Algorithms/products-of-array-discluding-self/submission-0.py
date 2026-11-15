class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ok lets do prefix sums, up to the number but not num
        # lets try doing one with the list up to num, and then reverse from eol up to num. we then multiply pref and suffix at that range
        prefix = [1]
        suffix = [1]
        
           
        for j in range(0, len(nums) - 1):
            prefix.append(prefix[-1] * nums[j])
        for k in range(len(nums) - 1, 0, -1):
            suffix.append(suffix[-1] * nums[k])
        suffix = suffix[::-1]
        for i in range(0, len(prefix)):
            prefix[i] *= suffix[i]
        
        return prefix
