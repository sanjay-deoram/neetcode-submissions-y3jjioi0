class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = Counter(nums)
        # {5:4, 3: 2, 1:1}
        max_value = float('-inf')

        for idx, val in enumerate(element_count):
            if element_count[val] > len(nums)//2:
                return val
        return max_value