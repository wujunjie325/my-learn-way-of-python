maze = [[1,0,1,1,0,0,0,1,3],
        [1,0,0,0,1,1,0,0,0],
        [0,0,1,1,0,0,0,1,0],
        [1,0,1,0,0,1,0,0,1],
        [2,0,0,0,0,1,0,0,1]]
#面向对象改写
class Find_entry():
    def __init__(self, maze):
        self.maze = maze
        self.m = len(maze)
        self.n = len(maze[0])
        self.map = [[0] * self.n for _ in range(self.m)]
        self.path = []


    def find_start(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.maze[i][j] == 2:
                    return (i, j)
        

    def find_end(self, start_m, start_n, path):
        if start_m < 0 or start_n < 0 or start_m >= self.m or start_n >= self.n:
            return False
        if self.maze[start_m][start_n] == 1 or self.map[start_m][start_n] == 1:
            return False
        if self.maze[start_m][start_n] == 3:
            return (True, path)
        self.map[start_m][start_n] = 1
        return self.find_end(start_m + 1, start_n, path + [[start_m + 1,start_n]]) or \
                self.find_end(start_m - 1, start_n, path + [[start_m - 1,start_n]]) or \
                self.find_end(start_m, start_n + 1, path + [[start_m,start_n + 1]]) or \
                self.find_end(start_m, start_n - 1, path + [[start_m,start_n - 1]])


def main():
    a = Find_entry(maze)
    start = a.find_start()
    ans = a.find_end(start[0], start[1], [list(start)])
    if ans != False:
        print(ans[0])
        print(ans[1])
    else:
        print(ans)


if __name__ == "__main__":
    main()