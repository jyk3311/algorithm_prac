from collections import deque

def bfs_queue(graph, start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited


def dfs_recursive(graph, node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(graph, adj, visited)

    return visited


def dfs_stack(graph, start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited


#DFS
def island_dfs_recursive(grid):
    #마찬가지로 상하좌우 살펴보는 변수
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    #col, row 길이
    m = len(grid)
    n = len(grid[0])

    cnt = 0

    #섬 하나를 바다로 바꾸는 함수. 밑에 for문을 먼저보고 이 함수를 보면 이해가 빠릅니다.
    def dfs_recursive(r, c):
        # 방문한 노드의 상하좌우를 살피는데 배열에 크기에 벗어나거나, 육지가 아니면 스킵
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        #상하좌우 살펴보다가 육지 발견하면 반복
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    #전체 배열을 방문함
    for r in range(m):
        for c in range(n):
            #node라는 빈 변수에 grid[r][c]가 1이 나올때까지 스킵
            node = grid[r][c]
            if node != '1':
                continue

            #node에 1이 나와 저장하면 육지 발견. 섬 하나로 간주 후, 그 섬 하나를 바다로 바꿈
            cnt += 1
            #섬 하나를 바다로 바꾸는 함수
            dfs_recursive(r, c)

    return cnt
def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt



#이진탐색 함수
def binary_search(nums, target):
    def bs(start, end):

        #비교를 다했음에도 불구하고 값이 없던 것
        if start > end:
            return -1

        mid = (start + end) // 2

        #가운데 값보다 크면 가운데서부터 끝 사이의 가운데를 비교
        if nums[mid] < target:
            return bs(mid + 1, end)
        #가운데 값보다 작으면 처음부터 가운데 사이의 가운데를 비교
        elif nums[mid] > target:
            return bs(start, mid - 1)
        #같은 값을 찾았으므로 가운데 값 반환
        else:
            return mid

    return bs(0, len(nums) - 1)