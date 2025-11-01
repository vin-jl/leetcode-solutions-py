class Solution:
    def jump(self, nums: List[int]) -> int:
        """ slow dp solution
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for j in range(nums[i]+1):
                if i+j < n:
                    dp[i+j] = min(dp[i]+1, dp[i+j])

        return dp[n-1]
        """
        count = 0 # stores num of jumps
        farthest = 0 # stores the farthest i can go with count jumps
        currentEnd = 0 # add a jump when i reach the end of a range
        n = len(nums)
        for i in range(n-1):
            farthest = max(farthest, i+nums[i]) # update farthest range
            if i == currentEnd: # must jump
                count += 1
                currentEnd = farthest
                if currentEnd >= n-1:
                    break
        return count
