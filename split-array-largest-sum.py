class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canFill(nums: List[int], maxBag: int, k: int) -> bool:
            bags = 1
            curSum = 0
            for num in nums:
                if curSum + num > maxBag:
                    bags += 1
                    curSum = num
                else:
                    curSum += num
            return bags <= k
        
        low = max(nums)
        high = sum(nums)
        best = 0
        while low <= high:
            mid = low + floor((high-low)/2)
            if canFill(nums, mid, k):
                best = mid
                high = mid-1               
            else:
                low = mid+1
        return best
