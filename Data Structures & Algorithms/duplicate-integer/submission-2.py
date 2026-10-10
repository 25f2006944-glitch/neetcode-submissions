class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dict={}
        # for k in nums:
        #     if k in dict:
        #         dict[k]+=1
        #         if dict[k]>1:
        #             return True
        #     else:
        #         dict[k]=1
        # return False

        d=dict()
        for k in nums:
            d[k]=d.get(k,0)+1
            if d[k]>1:
                return True
        return False




