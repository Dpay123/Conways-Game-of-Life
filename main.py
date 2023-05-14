import random, time, copy

class Board:
    def __init__(self, w=60, h=20):
        self.width = w
        self.height = h
        self.cells = []

    def set_random(self):
        for x in range(self.height):
            column = []
            for y in range(self.width):
                if random.randint(0, 1) == 0:
                    column.append('[O]')
                else:
                    column.append('[ ]')
            self.cells.append(column)
    def set_glider(self):
        for x in range(self.height):
            column = []
            for y in range(self.width):
                if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
                    column.append('[O]')
                else:
                    column.append('[ ]')
            self.cells.append(column)

    def show_board(self):
        print('\n\n')
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
                    left = (y - 1) % self.width
                    right = (y + 1) % self.width
                    up = (x - 1) % self.height
                    down = (x + 1) % self.height

                    numNeighbors = 0
                    if currentCells[up][left] == '[O]':
                        numNeighbors += 1
                    if currentCells[up][y] == '[O]':
                        numNeighbors += 1
                    if currentCells[up][right] == '[O]':
                        numNeighbors += 1
                    if currentCells[x][left] == '[O]':
                        numNeighbors += 1
                    if currentCells[x][right] == '[O]':
                        numNeighbors += 1
                    if currentCells[down][left] == '[O]':
                        numNeighbors += 1
                    if currentCells[down][y] == '[O]':
                        numNeighbors += 1
                    if currentCells[down][right] == '[O]':
                        numNeighbors += 1

                    cell = currentCells[x][y]

                    if cell == '[O]' and numNeighbors in [2, 3]:
                        continue
                    elif cell == '[ ]' and numNeighbors == 3:
                        self.cells[x][y] = '[O]'
                    else:
                        self.cells[x][y] = '[ ]'

            time.sleep(.5)



if __name__ == '__main__':
    print('Conways Game of Life')
    board = Board()
    while True:
        print('Choose an option:' + '\n(r)andom' + '\n(g)lider')
        choice = input()
        if choice == 'r':
            board.set_random()
            break
        elif choice == 'g':
            board.set_glider()
            break
    board.run()