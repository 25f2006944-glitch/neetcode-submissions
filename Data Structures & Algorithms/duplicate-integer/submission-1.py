class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for k in nums:
            if k in dict:
                dict[k]+=1
                if dict[k]>1:
                    return True
            else:
                dict[k]=1
        return False