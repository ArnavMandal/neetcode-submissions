class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ok so we know that anagrams are wordss with same letters,
        # so if they are sorted they should technically be the same
        # but optimized, we jsut need the freq of each letter of the
        # word, so basically if we make a count of each letter and make?
        # it a key, we can just append each word like that

        from collections import defaultdict

        out = defaultdict(list)
        for w in strs:

            count = [0] * 26

            for c in w:
                count[ord(c) - ord('a')]+=1
            out[tuple(count)].append(w)
        return list(out.values())