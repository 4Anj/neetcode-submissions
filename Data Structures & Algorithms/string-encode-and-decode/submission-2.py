class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i<len(s):
            j=s.index("#",i)
            l=int(s[i:j])
            st=j+1
            en=st+l
            d=s[st:en]
            i=en
            res.append(d)
        return res