class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, subSet = [],[]
        return self.helper(0,nums, currSet, subSet)

        
    def helper(self,i,nums, currSet, subSet):
        
        # how do we know when to add it to subSet?
        # here we know that once i has passed the length that its reached the leaf/end
        if i >= len(nums):
            subSet.append(currSet.copy())
            return

        currSet.append(nums[i])
        self.helper(i+1, nums, currSet,subSet)
        currSet.pop()
        self.helper(i+1, nums, currSet,subSet)
        return subSet