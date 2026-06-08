class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer algo
        count, res = 0, 0
        prev = nums[0]

        for i in range(len(nums)):
            if count == 0 or nums[i] == prev:
                res = nums[i]
                count += 1
            if nums[i]!=prev:
                count-=1
            
            print(f"Count:{count} | res: {res} | i:{i} | nums[i]:{nums[i]}")
        return res
