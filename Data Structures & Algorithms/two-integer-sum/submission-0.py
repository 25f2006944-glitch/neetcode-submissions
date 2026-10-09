class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i+j==target:
                    l.append(nums.index(i))
                    l.append(nums.index(j))
        return sorted(l)