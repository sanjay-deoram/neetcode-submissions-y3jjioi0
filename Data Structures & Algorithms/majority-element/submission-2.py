class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = Counter(nums)
        # {5:4, 3: 2, 1:1}
        max_value = float('-inf')

        for key, val in element_count.items():
            if element_count[key] > len(nums)//2:
                return key
        return 0