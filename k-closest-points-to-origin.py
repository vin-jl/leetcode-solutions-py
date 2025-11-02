class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point : sqrt((point[0] - 0)**2 + (point[1] - 0) ** 2))
        """
        result = []
        for i in range(k):
            result.append(points[i])
        return result
        """
        return points[:k]
