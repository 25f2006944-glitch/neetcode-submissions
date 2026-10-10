class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=dict()
        d2=dict()
        for k in s:
            d1[k]=d1.get(k,0)+1
        for k in t:
            d2[k]=d2.get(k,0)+1
        if d1==d2:
            return True
        return False