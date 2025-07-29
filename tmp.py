from typing import List
from collections import deque, defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Hàm thực hiện topological sort sử dụng Kahn's Algorithm
        def topological_sort(k: int, conditions: List[List[int]]) -> List[int]:
            print('='*10)
            print(f"Processing conditions: {conditions}")
            # Khởi tạo đồ thị và bậc vào
            adj = defaultdict(list)
            indegree = [0] * (k + 1)  # Bỏ qua index 0, dùng từ 1 đến k
            for a, b in conditions:
                print(f"Adding edge from {a} to {b}")
                adj[a].append(b)
                indegree[b] += 1
                print(f"Adjacency list: {dict(adj)}")
                print(f"Indegree: {indegree[:]}")
            
            # Khởi tạo hàng đợi với các node có bậc vào bằng 0
            queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            print(f"Initial queue: {queue}")
            order = []
            
            # Xử lý hàng đợi
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                print(f"Processed node: {node}, Current order: {order}")
            # Nếu số node trong order không đủ k, có chu trình, trả về danh sách rỗng
            return order if len(order) == k else []
        
        # Lấy thứ tự định hướng cho hàng và cột
        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)
        print(f"Row order: {row_order}, Column order: {col_order}")
        # Nếu một trong hai không hợp lệ (có chu trình), trả về ma trận rỗng
        if not row_order or not col_order:
            return []
        
        # Xây dựng ma trận
        matrix = [[0] * k for _ in range(k)]
        # Tạo ánh xạ từ giá trị sang chỉ số hàng và cột
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        # Đặt các số vào ma trận
        for num in range(1, k + 1):
            if num not in row_pos or num not in col_pos:
                return []
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix
    
# Example usage:
col_conditions = [[2,1],[3,2]]
row_conditions = [[1,2],[3,2]]
solution = Solution()
result = solution.buildMatrix(3, row_conditions, col_conditions)
print(result)  # Output: [[1, 2, 3], [0, 0, 0], [0, 0, 0]] or similar valid matrix