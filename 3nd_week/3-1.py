from collections import deque


def escape_maze(m):
    N, M = len(m), len(m[0])#행과 열의 크기
    visited = [[False] * M for i in range(N)]
    queue = deque([(0,0,1)])#방문해야하는 곳과 길이
    visited[0][0] = True

    derections = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x, y, dist = queue.popleft()
        if x == N-1 and y == M-1:
            return dist

        for dx, dy in derections:
            nx ,ny= x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and m[nx][ny] == "1":
                visited[nx][ny] = True
                queue.append((nx,ny,dist + 1))


    return -1







# 예시 입력
maze = [
    "11101",
    "10101",
    "10101",
    "11111"
]

# 문자열을 리스트로 변환하여 입력
maze = [list(row) for row in maze]

# 함수 실행 및 결과 출력
print(escape_maze(maze))