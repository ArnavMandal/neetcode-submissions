class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ok lets use a bucket sort here, so we can 
        # make an array of counts from 0 to len(nums)
        # and put frequencies of each number into it
        # we then search thru that list for the top k elements
        
        count = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] += 1
        for key, v in count.items():
                buckets[v].append(key)
        res = []
        buckets = buckets[::-1]

        for b in buckets:
            if b != 0:
                for num in b:
                    res.append(num)
            if len(res) == k:
                return res
        
        
