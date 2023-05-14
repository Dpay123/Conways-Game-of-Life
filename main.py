import random, time, copy

class Board:
    def __init__(self, w=60, h=20):
        self.width = w
        self.height = h
        self.cells = []
        self.set_random()

    def set_random(self):
        for x in range(self.height):
            column = []
            for y in range(self.width):
                if random.randint(0, 1) == 0:
                    column.append('#')
                else:
                    column.append(' ')
            self.cells.append(column)

    def show_board(self):
        print('\n\n\n\n\n')
        for x in range(self.height):
            for y in range(self.width):
                print(self.cells[x][y], end='')
            print()

    def run(self):
        while True:
            self.show_board()
            currentCells = copy.deepcopy(self.cells)

            for x in range(self.height):
                for y in range(self.width):
                    left = max(0, y - 1)
                    right = min(y + 1, self.width - 1)
                    up = max(0, x - 1)
                    down = min(x + 1, self.height - 1)

                    numNeighbors = 0
                    if currentCells[up][left] == '#':
                        numNeighbors += 1
                    if currentCells[up][y] == '#':
                        numNeighbors += 1
                    if currentCells[up][right] == '#':
                        numNeighbors += 1
                    if currentCells[x][left] == '#':
                        numNeighbors += 1
                    if currentCells[x][right] == '#':
                        numNeighbors += 1
                    if currentCells[down][left] == '#':
                        numNeighbors += 1
                    if currentCells[down][y] == '#':
                        numNeighbors += 1
                    if currentCells[down][right] == '#':
                        numNeighbors += 1

                    cell = currentCells[x][y]

                    if cell == '#' and numNeighbors in [2, 3]:
                        continue
                    elif cell == ' ' and numNeighbors == 3:
                        self.cells[x][y] = '#'
                    else:
                        self.cells[x][y] = ' '

            time.sleep(0.5)



if __name__ == '__main__':
    print('Conways Game of Life')
    board = Board()
    board.run()