# Solve sudoku puzzle
# python solve_a_sudoku.py


ALLOWED_VALUES = list(range(1, 10))
PUZZLE_INDICES = list(range(9))
BOX_INDICES = list(range(3))


def solve_sudoku(puzzle):
    '''
    Solve a sudoku

    Arguments:
        puzzle (list): partially solved sudoku

    Returns
        puzzle (list): solved sudoku
    '''
    for row in PUZZLE_INDICES:
        for column in PUZZLE_INDICES:
            if puzzle[row][column] == 0:
                for number in ALLOWED_VALUES:
                    allowed = True

                    # check in row
                    for i in PUZZLE_INDICES:
                        if puzzle[i][column] == number:
                            allowed = False
                            break

                    # check in column
                    for j in PUZZLE_INDICES:
                        if puzzle[row][j] == number:
                            allowed = False
                            break

                    # check in box     
                    for i in BOX_INDICES:
                         for j in BOX_INDICES:
                            if puzzle[row - (row % len(BOX_INDICES)) + i][column - (column % len(BOX_INDICES)) + j] == number:
                                allowed = False
                                break                

                    if allowed:       
                        puzzle[row][column] = number
                        trial = solve_sudoku(puzzle)
                        if trial != False:
                            return trial
                        else:
                            puzzle[row][column] = 0
                return False
    return puzzle
    

def print_sudoku(puzzle):
    '''
    Print a sudoku puzzle in a nice visualization

    Arguments:
        puzzle (list): sudoku puzzle

    Returns
        None
    '''
    for row in PUZZLE_INDICES:
        if ((row % len(BOX_INDICES) == 0)):
            print('-' * (len(PUZZLE_INDICES) * 3 - 2))
        for column in PUZZLE_INDICES:
            if ((column % len(BOX_INDICES) == 0)):
                if (column == 0):
                    print('|', end = '')
                else:
                    print(' |', end = '')
            if puzzle[row][column] == 0:
                print('  ', end = '')
            else:
                print(' {}'.format(puzzle[row][column]), end = '')
        print(' |')
    print('-' * (len(PUZZLE_INDICES) * 3 - 2))


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0]
                , [6, 0, 0, 1, 9, 5, 0, 0, 0]
                , [0, 9, 8, 0, 0, 0, 0, 6, 0]
                , [8, 0, 0, 0, 6, 0, 0, 0, 3]
                , [4, 0, 0, 8, 0, 3, 0, 0, 1]
                , [7, 0, 0, 0, 2, 0, 0, 0, 6]
                , [0, 6, 0, 0, 0, 0, 2, 8, 0]
                , [0, 0, 0, 4, 1, 9, 0, 0, 5]
                , [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print('Puzzle:')
    print_sudoku(puzzle)
    print('Solved:')
    print_sudoku(solve_sudoku(puzzle))
