# SUDOKU solver test
# main program for testing my sudoku solver class inside sudoku_np1
# Version 0.01, WSC, 6-Nov-2024

# read a string representing a 9x9 SUDOKU into a numpy array

from sudoku_np1 import sudoku
from sudoku_io import sudoku_io

import time

# ===== currently not solved
SuTextInt=[]
suCommentInt=[]
SuTextInt.append(".9.7..86..31..5.2.8.6........7.5...6...3.7...5...1.7........1.9.2.6..35..54..8.7.")
suCommentInt.append("diabolical, solving sudoku, m. mepham")

# the number of the sudoku that should be tested
TEST_SUDOKU_NUM = 13

MAX_GUESS_NUM = 1000

PRINT_SUDOKU = False
TEST_SUDOKU_FUNC = False
TEST_SUDOKU_CAND = False
TEST_SUDOKU_LONE = False
TEST_SUDOKU_HIDDEN_SINGLE = False
TEST_SUDOKU_SOLVER = False
TEST_SUDOKU_SOLVER_ALL = True

myIo = sudoku_io()
myIo.readFile("sudoku_1.txt")
suText, suComment = myIo.getSudokuList()

if __name__ == '__main__':
    print(f"Total of {len(suText)} Sudokus available")
    if TEST_SUDOKU_NUM<0:
        TEST_SUDOKU_NUM=0
    if TEST_SUDOKU_NUM>=len(suText):
        TEST_SUDOKU_NUM=len(suText)-1
    mySudoku = sudoku()
    mySudoku.setSuArray(suText[TEST_SUDOKU_NUM])
    mySudoku.setComment(suComment[TEST_SUDOKU_NUM])

    if PRINT_SUDOKU:
        print(f"SUDOKU number: {TEST_SUDOKU_NUM}")
        mySudoku.printComment() 
        mySudoku.print()

    if TEST_SUDOKU_FUNC:
        for i in range(0,9):
            mySudoku.printValListInBlock(i)
        for i in range(0,9):
            mySudoku.printValListInRow(i)
        for i in range(0,9):
            mySudoku.printValListInCol(i)

    if TEST_SUDOKU_CAND:
        mySudoku.calcAllCandidateList()
        mySudoku.printAllCandidateList()      

    if TEST_SUDOKU_LONE:
         mySudoku.findLonePairs()

    if TEST_SUDOKU_HIDDEN_SINGLE:
        mySudoku.findHiddenSingles()
        mySudoku.print()

    # run solver just with solveSingles() algorithm
    if TEST_SUDOKU_SOLVER:
        print(f"==================== Sudoku number {TEST_SUDOKU_NUM} ========================================")
        mySudoku = sudoku()
        mySudoku.setSuArray(suText[TEST_SUDOKU_NUM])
        mySudoku.setComment(suComment[TEST_SUDOKU_NUM])
        mySudoku.print()
        mySudoku.printComment()

        startTime = time.time()
        debug = False
 
        solved1 = mySudoku.solver1(debug)
        if not solved1:
           solved2, num_guesses = mySudoku.solver2(MAX_GUESS_NUM)
     
        endTime =time.time()
        if solved1:
            print(f"SUCCESS: Sudoku is solved with SOLVER1, elapsed time is {endTime-startTime:.3f}")
        elif solved2:
            print(f"Info: total of {num_guesses} guess loops done")
            print(f"SUCCESS: Sudoku is solved with SOLVER2, elapsed time is {endTime-startTime:.3f}")
        else:
            print(f"FAIL:    No Sudoku solution found with SOLVER2, elapsed time is {endTime-startTime:.3f}")
        
            
        mySudoku.print()

    PRINT_SOLUTIONS = True
    if TEST_SUDOKU_SOLVER_ALL:
        debug = False
        for i in range(0,len(suText)):
            print(f"==================== Sudoku number {i} ========================================")
            mySudoku = sudoku()
            mySudoku.setSuArray(suText[i])
            mySudoku.setComment(suComment[i])
            print(suComment[i])
            startTime = time.time()
    
            solved1 = mySudoku.solver1(debug)
            if not solved1:
                solved2, num_guesses = mySudoku.solver2(MAX_GUESS_NUM,debug)       
            endTime =time.time()
            if solved1:
                print(f"SUCCESS: Sudoku is solved with SOLVER1, elapsed time is {endTime-startTime:.3f}")
            elif solved2:
                print(f"Info: total of {num_guesses} guess loops done")
                print(f"SUCCESS: Sudoku is solved with SOLVER2, elapsed time is {endTime-startTime:.3f}")
            else:
                print(f"FAIL:    No Sudoku solution found with SOLVER2, elapsed time is {endTime-startTime:.3f}")           

            if PRINT_SOLUTIONS:
                mySudoku.print()


