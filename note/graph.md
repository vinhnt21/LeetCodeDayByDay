---
markmap:
  colorFreezeLevel: 2
  initialExpandLevel: 2
  maxWidth: 400
---

# 🗺️ Đồ Thị (Graph) cho AI & AI Agent

## I. Kiến thức Nền tảng 🧠

### 1. Định nghĩa & Thành phần
- **Bản chất**: Đồ thị là một cách biểu diễn các đối tượng và mối quan hệ giữa chúng.
  - **Đỉnh (Node/Vertex)**: Đại diện cho một đối tượng.
    - *Ví dụ*: Người dùng, thành phố, trạng thái game, từ ngữ.
  - **Cạnh (Edge)**: Đại diện cho mối quan hệ giữa hai đối tượng (đỉnh).
    - *Ví dụ*: Quan hệ bạn bè, đường đi, hành động, sự liên quan.
- **Phân loại quan trọng**
  - **Vô hướng (Undirected)**: Quan hệ hai chiều (A-B). *Ví dụ: Bạn bè trên Facebook.*
  - **Có hướng (Directed)**: Quan hệ một chiều (A -> B). *Ví dụ: Follow trên Twitter.*
  - **Có trọng số (Weighted)**: Cạnh có một giá trị (chi phí, khoảng cách). *Ví dụ: Khoảng cách giữa 2 thành phố.*
  - **Không trọng số (Unweighted)**: Các cạnh như nhau, chỉ thể hiện sự tồn tại của liên kết.

### 2. Biểu diễn đồ thị
- **Danh sách Kề (Adjacency List)**
  - **Bản chất**: Một từ điển (dictionary/map) mà mỗi key là một đỉnh, và value là một danh sách các đỉnh kề với nó.
  - **Ưu điểm**: Tiết kiệm bộ nhớ cho đồ thị thưa (ít cạnh).
  - **Mã Python**:
    ```python
    # {đỉnh: [hàng_xóm_1, hàng_xóm_2,...]}
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B']
    }
    ```
- **Ma trận Kề (Adjacency Matrix)**
  - **Bản chất**: Một ma trận vuông `N x N` (N là số đỉnh). `matrix[i][j] = 1` (hoặc trọng số) nếu có cạnh từ i đến j.
  - **Ưu điểm**: Kiểm tra sự tồn tại của cạnh giữa 2 đỉnh rất nhanh (O(1)).
  - **Mã Python**:
    ```python
    #     A B C D
    # A [[0,1,1,0],
    # B  [1,0,0,1],
    # C  [1,0,0,0],
    # D  [0,1,0,0]]
    adj_matrix = [[0,1,1,0], [1,0,0,1], [1,0,0,0], [0,1,0,0]]
    ```
### 3. Thuật toán Duyệt đồ thị
- **DFS (Depth-First Search)**
  - **Bản chất**: Ưu tiên đi "sâu" nhất có thể theo một nhánh, dùng **Stack** (hoặc đệ quy).
  - **Luồng hoạt động**:
    1. Đưa đỉnh bắt đầu vào Stack.
    2. Lấy một đỉnh ra khỏi Stack, đánh dấu đã thăm.
    3. Đưa tất cả hàng xóm **chưa được thăm** của đỉnh đó vào Stack.
    4. Lặp lại cho đến khi Stack rỗng.
  - **Mã Python (Đệ quy)**:
    ```python
    visited = set()
    def dfs(graph, node):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                dfs(graph, neighbour)
    ```
- **BFS (Breadth-First Search)**
  - **Bản chất**: Khám phá các đỉnh theo từng lớp (level), dùng **Queue**. Tìm đường đi ngắn nhất trên đồ thị không trọng số.
  - **Luồng hoạt động**:
    1. Đưa đỉnh bắt đầu vào Queue.
    2. Lấy một đỉnh ra khỏi Queue, đánh dấu đã thăm.
    3. Đưa tất cả hàng xóm **chưa được thăm** của đỉnh đó vào Queue.
    4. Lặp lại cho đến khi Queue rỗng.
  - **Mã Python**:
    ```python
    from collections import deque
    def bfs(graph, start_node):
        visited = {start_node}
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            print(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
    ```

## II. Tìm đường đi (Pathfinding) 🗺️

### 1. Thuật toán không Heuristic
- **Dijkstra**
  - **Bản chất**: Tìm đường đi ngắn nhất từ một đỉnh nguồn đến tất cả các đỉnh khác trong đồ thị có **trọng số không âm**. Thuật toán "tham lam" bằng cách luôn chọn đỉnh có khoảng cách tạm thời nhỏ nhất để khám phá.
  - **Cấu trúc dữ liệu chính**: **Priority Queue** (Hàng đợi ưu tiên).
  - **Luồng hoạt động**:
    1. Khởi tạo khoảng cách tới mọi đỉnh là vô cực (∞), đỉnh nguồn là 0.
    2. Đưa `(0, nguồn)` vào Priority Queue.
    3. Khi PQ chưa rỗng, lấy ra đỉnh `u` có khoảng cách nhỏ nhất.
    4. Với mỗi hàng xóm `v` của `u`, "relax" cạnh: nếu `dist[u] + weight(u,v) < dist[v]`, cập nhật `dist[v]` và đưa `(dist[v], v)` vào PQ.
  - **Mã Python (Ý tưởng)**:
    ```python
    import heapq
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]: continue
            for neighbor, weight in graph[node].items():
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return distances
    ```

### 2. Thuật toán có Heuristic (Cho AI)
- **A* (A-Star)**
  - **Bản chất**: "Phiên bản thông minh" của Dijkstra. Nó không chỉ xem xét chi phí đã đi (`g(n)`) mà còn cả chi phí **ước tính** để đến đích (`h(n)`). Cực kỳ quan trọng cho AI Agent.
  - **Công thức vàng**: `f(n) = g(n) + h(n)`
    - `f(n)`: Tổng chi phí ước tính (dùng để sắp xếp trong Priority Queue).
    - `g(n)`: Chi phí thực tế từ điểm bắt đầu đến `n` (phần của Dijkstra).
    - `h(n)`: Chi phí ước tính (heuristic) từ `n` đến đích. *Ví dụ: khoảng cách đường chim bay*.
  - **Điều kiện Heuristic**: `h(n)` phải "admissible", tức là không bao giờ ước tính cao hơn chi phí thực tế.
  - **Luồng hoạt động**: Tương tự Dijkstra nhưng Priority Queue sắp xếp theo `f(n)`.

## III. Biểu diễn Tri thức & Lập kế hoạch 🤖

### 1. Biểu diễn Tri thức
- **Đồ thị Tri thức (Knowledge Graph)**
  - **Bản chất**: Biểu diễn kiến thức thực tế dưới dạng các bộ ba `(chủ thể, vị ngữ, tân ngữ)` hay `(head, relation, tail)`.
  - **Ví dụ**:
    - `(Sơn Tùng M-TP, is_a, Singer)`
    - `(Hanoi, is_capital_of, Vietnam)`
    - `(Quỳnh Trang, có_biệt_danh_là, cái nịt)`
  - **Ứng dụng**: Nền tảng của Google Search, Siri, Alexa. Giúp máy "hiểu" thế giới.

### 2. Lập kế hoạch
- **Đồ thị Không gian Trạng thái (State Space Graph)**
  - **Bản chất**: "Bản đồ" tất cả các kịch bản có thể xảy ra.
    - **Đỉnh**: Mỗi trạng thái (state) của vấn đề (ví dụ: một thế cờ, vị trí robot).
    - **Cạnh**: Mỗi hành động (action) làm thay đổi trạng thái.
  - **Mục tiêu của Agent**: Tìm một đường đi (chuỗi hành động) trên đồ thị này từ trạng thái bắt đầu đến trạng thái mục tiêu, thường dùng các thuật toán tìm đường như A*.

## IV. Các bài toán Đồ thị quan trọng khác

### 1. Cây khung nhỏ nhất (MST)
- **Bản chất**: Tìm một tập hợp các cạnh để nối tất cả các đỉnh lại với nhau mà không tạo ra chu trình và có tổng trọng số là nhỏ nhất.
- **Ứng dụng**: Thiết kế mạng lưới (điện, viễn thông) với chi phí tối thiểu.
- **Thuật toán Kruskal**:
  - **Luồng**: Sắp xếp tất cả các cạnh theo trọng số tăng dần. Lần lượt thêm cạnh vào cây nếu nó không tạo ra chu trình (dùng cấu trúc Union-Find để kiểm tra).
- **Thuật toán Prim**:
  - **Luồng**: Bắt đầu từ một đỉnh. Liên tục chọn cạnh rẻ nhất nối một đỉnh *đã trong cây* với một đỉnh *chưa trong cây* (dùng Priority Queue).

### 2. Thành phần liên thông mạnh (SCC)
- **Bản chất**: Trong đồ thị có hướng, SCC là một tập hợp các đỉnh mà từ bất kỳ đỉnh nào trong đó cũng có đường đi đến bất kỳ đỉnh nào khác trong cùng tập hợp.
- **Thuật toán**: Tarjan's, Kosaraju's.
- **Ứng dụng**: Phân tích mạng xã hội, các mối quan hệ tương hỗ.

## V. Ứng dụng cho AI Agent 🚀
- **Tìm đường**: Robot di chuyển trong kho hàng (Dijkstra, A*).
- **Lập kế hoạch**: Agent giải game puzzle (tìm đường trên State Space Graph).
- **Ra quyết định**: AI chơi game đối kháng như cờ vua (dùng cây Minimax, một dạng đồ thị cây).
- **Xử lý ngôn ngữ tự nhiên (NLP)**:
  - **Đồ thị phụ thuộc (Dependency Graph)**: Phân tích cấu trúc ngữ pháp của câu.
- **Hệ thống Gợi ý (Recommender Systems)**:
  - Dùng đồ thị để biểu diễn người dùng và sản phẩm, dự đoán các cạnh còn thiếu (gợi ý sản phẩm).
- **Mạng Nơ-ron Đồ thị (GNNs)**:
  - **Deep Learning trên đồ thị**: Áp dụng cho các bài toán mà dữ liệu có cấu trúc đồ thị tự nhiên (phân tích mạng xã hội, hóa học...).

## VI. Tài liệu & Thực hành 📚
- **Sách gối đầu giường**:
  - *AI: A Modern Approach* (Stuart Russell, Peter Norvig)
  - *Grokking Algorithms* (Aditya Bhargava)
- **Thực hành (LeetCode/Codewars)**:
  - Các bài toán về DFS, BFS.
  - Các bài toán về Dijkstra, A*.
  - Các bài toán về Union-Find (cho MST).
  - *Ví dụ kinh điển*: 997. Find the Town Judge.