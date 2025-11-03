class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range(len(nums)):
            if nums[i] in find:
                return [find.get(nums[i]), i]
            else:
                find[target-nums[i]] = i
