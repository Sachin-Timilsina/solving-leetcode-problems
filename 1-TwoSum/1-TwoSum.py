class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index, first_number in enumerate(nums):
            for second_index in range(len(nums)):
                if first_index is not second_index:
                    if (first_number + nums[second_index]) == target:
                        return [first_index, second_index]
