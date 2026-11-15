class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out = out + "#$^%@#" + s
        return out
    def decode(self, s: str) -> List[str]:
        out = s.split("#$^%@#")
        return out[1:]