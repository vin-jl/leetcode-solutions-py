class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        setnum = set()
        for i in range(len(nums)):
            setnum.add(nums[i])
            if len(setnum) == i:
                return nums[i]
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow = 0
        while slow!= fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
