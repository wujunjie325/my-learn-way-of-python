class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open (mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

    def searchFrom(self, maze, startRow,startColumn):
        maze.updatePosition(startRow, startColumn)
        if maze[startRow][startColumn] == OBSTACLE:
            return False

        if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
            return False

        if maze.isExit(startRow,startColumn):
            maze.updatePosition(startRow, startColumn, PART_OF_PATH)
            return True

        maze.updatePosition(startRow, startColumn , TRIED)

        found = searchFrom(maze, startRow - 1 , startColumn) or \
                searchFrom(maze, startRow + 1 , startColumn) or \
                searchFrom(maze, startRow, startColumn - 1) or \
                searchFrom(maze, startRow - 1 , startColumn + 1)

        if found:
            maze.updatePosition(startRow, startRow, PART_OF_PATH)
        else:
            maze.updatePosition(startRow, startRow, DEAD_END)
        return found 