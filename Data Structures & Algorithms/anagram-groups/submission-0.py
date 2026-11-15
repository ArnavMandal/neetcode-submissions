class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = defaultdict(list)

        for word in strs:

            key = ''.join(sorted(word))

            out[key].append(word)
        
        return list(out.values())
            



