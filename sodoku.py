def find_next_empty(puzzel):


     for r in range (9):
          for c in range(9):
               if puzzel[r][c] == -1:  
                  return r, c
               
     return None, None


def is_valid(puzzel, guess, row, col):

    row_vals = puzzel[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzel[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzel[r][c] == guess:
                return False
            
    return True

def sodoku_solver(puzzel):
    

    row, col = find_next_empty(puzzel)
   

    if row is None:
       return True
    

    for guess in range(1,10):

        if is_valid(puzzel, guess,row, col):
            puzzel[row][col] = guess

            if sodoku_solver(puzzel):
                return True
            

        puzzel[row][col] = -1
    return False

if __name__ == '__main__':
    example_board = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],

    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],

    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

    
    print(sodoku_solver(example_board))
    print(example_board)