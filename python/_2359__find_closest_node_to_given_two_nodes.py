from typing import *

class Solution:
    def closestMeetingNode(self, edges: List[int],
                           node1: int, node2: int) -> int:
        n = len(edges)

        # Hàm phụ: khoảng cách từ một nguồn
        def calc(src: int) -> List[int]:
            print(f"Calculating distances from node {src}")
            dist = [-1] * n
            print(f"Initial distances: {dist}")
            cur, d = src, 0
            
            while cur != -1 and dist[cur] == -1:
                print(f"Visiting node {cur} at distance {d}")
                dist[cur] = d
                cur = edges[cur]
                d += 1
            return dist

        dist1 = calc(node1)
        print(dist1)
        dist2 = calc(node2)
        print(dist2)
        best, bestMax = -1, float('inf')
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                curMax = max(dist1[i], dist2[i])
                if curMax < bestMax or (curMax == bestMax and i < best):
                    bestMax, best = curMax, i
        return best


# Example usage:
edges = [2, 2, 3, -1]
node1 = 0
node2 = 1
solution = Solution()
result = solution.closestMeetingNode(edges, node1, node2)
print(result)  # Output: 2
