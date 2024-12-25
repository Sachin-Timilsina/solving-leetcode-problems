class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for index, number in enumerate(nums):
            compliment = target - number
            if compliment in visited:
                return [index, visited[compliment]]
            visited[number] = index
