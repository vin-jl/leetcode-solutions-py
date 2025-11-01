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
        count = 0
        farthest = 0
        currentEnd = 0
        n = len(nums)
        for i in range(n-1):
            farthest = max(farthest, i+nums[i]) # check if jumping will go farther than cur
            if i == currentEnd: # have not explored further
                count += 1
                currentEnd = farthest
        return count
