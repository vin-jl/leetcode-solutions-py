class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range(len(nums)):
            if nums[i] in find:
                return [i, find.get(nums[i])]
            else:
                find[target-nums[i]] = i
