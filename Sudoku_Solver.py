import numpy as np
# use numpy library to format the sudoku as a matrix 

sudoku = np.matrix([[0,3,2,0,0,0,0,7,0], # sample sudoku with a solution
                   [0,0,0,2,1,9,5,0,0],
                   [0,0,0,7,0,0,1,0,2],
                   [8,0,1,0,0,0,0,4,5],
                   [3,4,0,0,0,1,0,0,6],
                   [2,5,0,4,0,0,8,0,0],
                   [4,0,0,5,0,0,0,1,3],
                   [0,1,5,3,4,0,6,0,0],
                   [6,8,0,1,9,0,2,0,4]])


def finding_zeros(sudoku):
    # this function checks the row and col to find where the first empty cell is. 
    # empty cells are denoted by 0 

        for row in range(0,9): 
            for col in range(0,9):
                if sudoku[row,col] == 0: # if the sudoku's position at row,col is 0 (empty) 
                    return row,col # return the row and column number where the empty cell occurs. 
                
                
        return None,None   # if there are no empty cells. 


def possible_value(test_number,row,col): # the first input will take a number and test to see if it works in a 
                                         # given position 

    
    for i in range(9): 
        if test_number == sudoku[row,i]: # checks if test_number occurs in the row which we found an empty cell for all coloumn values i.
            return(False)                # function will return false test_number does occur 
        
    for i in range(9): 
        if test_number == sudoku[i,col]: # checks if test_number occurs in the coloumn which we found an empty cell for all row values i.
            return(False)
    
    # now we check to see if the number occurs in the 3X3 grid in which test_number is in. 
    
    row_start = (row // 3)*3  
    col_start = (col // 3)*3
    
    by_3_matrix = [] 
    
    for r in range(row_start, row_start + 3): 
        for c in range(col_start, col_start + 3 ): 
            by_3_matrix.append(sudoku[r,c])
    if test_number in by_3_matrix:
        return(False)
    else: 
        return(True)

            
def solve(sudoku): # this function will solve the sudoku
    
    row,col = finding_zeros(sudoku)
    
    if row is None:  # finding zeros will return none if no empt cells are found. In that case the puzzle is solved. 
        return(True)
    
    
    
    for number in range(1,10): 
        test_number = number
        if possible_value(test_number, row, col) == True: # if possible_values returns a possible value, we set that position in the sudoku to a new number.
            sudoku[row,col] = number
            
            if solve(sudoku): # call the function recursively 
                return True
        
        sudoku[row,col] = 0
        
    
    return(False) # return false if there are no solutions 
                
solve(sudoku)

print(sudoku)

