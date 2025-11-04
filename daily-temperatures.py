class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] # pair of temp, index

        for i in range(n):
            cur = temperatures[i]
            while stack and cur > stack[-1][0]: # stack will always be decreasing
                temp, idx = stack.pop()
                result[idx] = i - idx

            stack.append([cur, i])

        return result
