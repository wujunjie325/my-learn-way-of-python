maze = [[1,0,1,1,0,0,0,1,3],
        [1,0,1,1,1,1,0,0,0],
        [0,1,0,1,0,0,0,1,0],
        [2,0,0,0,0,1,0,0,1]]

def find_Start(maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                return (i, j)
def create_token(maze):
    return [[0] * len(maze[0])for _ in range(len(maze))]

def find_end(maze, start_m, start_n, token, m, n, path):
    if start_m >= m or start_m < 0 or start_n >= n or start_n < 0:
        return False

    if maze[start_m][start_n] == 1:
        return False
    if token[start_m][start_n] == 1:
        return False
    if maze[start_m][start_n] == 3:
        return True, path
    token[start_m][start_n] = 1
    return find_end(maze, start_m + 1, start_n, token, m, n, path + [[start_m + 1, start_n]]) or\
            find_end(maze, start_m - 1, start_n, token, m, n, path + [[start_m - 1, start_n]]) or\
            find_end(maze, start_m, start_n + 1, token, m, n, path + [[start_m, start_n + 1]]) or\
            find_end(maze, start_m, start_n - 1, token, m, n, path + [[start_m, start_n - 1]])
token = create_token(maze)
start = find_Start(maze)
path = []
path.append([list(start)])
ans = find_end(maze, start[0], start[1],token, len(token), len(token[0]), path)
print(ans[0])
print(ans[1])
'''
print(path)
return find_end(maze, start_m + 1, start_n, token, m, n, path.append((start_m + 1, start_n))) or\
            find_end(maze, start_m - 1, start_n, token, m, n, path.append((start_m + 1, start_n))) or\
            find_end(maze, start_m, start_n + 1, token, m, n, path.append((start_m + 1, start_n))) or\
            find_end(maze, start_m, start_n - 1, token, m, n, path.append((start_m + 1, start_n)))
'''
