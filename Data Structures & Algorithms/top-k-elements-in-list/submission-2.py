from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        d=Counter(nums)
        top2=sorted(d,key=d.get,reverse=True)[:k]# if want both keys and valuessorted(d.items(), key=lambda x: x[1], reverse=True)
        return top2

        