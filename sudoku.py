#!/usr/local/bin/python3
# sudoku.py: program to solve SUDOKU and generate pretty print documentation
VERSION = "0.10"
# Version 0.10, WSC, 28-Dec-2024

from sudoku_np1 import sudoku_np1
from sudoku_io import sudoku_io
import sys

DEBUG_FLAG=False
SU_NUM_START=1
SU_NUM_STOP=SU_NUM_START+1
SU_NUM_ALL=False
PRINT_FLAG=True
MAX_GUESS_NUM = 100
USE_SOLVER2 = False

# parse input arguments
# example usage: $python sudoku_ex1.py -num=4
if len(sys.argv)>=2:
    for i in range(1,len(sys.argv)):
        actArg = sys.argv[i]
        if DEBUG_FLAG:
            print(f"... processing argument: {actArg}")
        if "-num" in actArg:
            n = int(actArg.replace("-num=", ""))
            SU_NUM_START=n
            SU_NUM_STOP=SU_NUM_START+1
        if "-start" in actArg:
            n = int(actArg.replace("-start=", ""))
            SU_NUM_START=n
            SU_NUM_STOP=SU_NUM_START+1
        if "-stop" in actArg:
            n = int(actArg.replace("-stop=", ""))
            SU_NUM_STOP=n+1
        if "-all" in actArg:
            SU_NUM_ALL=True
        if "-noprint" in actArg:
            PRINT_FLAG=False
        if "-help" in actArg:
            print("Optional arguments for sudoku_ex1:")
            print("    -help            ... print help")
            print("    -v               ... show program version")
            print("    -num=3           ... solve SUDOKU #3")
            print("    -start=3 -stop=8 ... solve SUDOKU #3 to #8")
            print("    -all             ... solve all SUDOKUs read from input file")
            print("    -noprint         ... no print of SUDOKU solution, just print PASS/FAIL results")
            sys.exit()
        if "-v" in actArg:
            print(f"    Welcome to sudoku_ex1, this is version {VERSION}")
            sys.exit()

# read the input file into arrays suText, suComment
myIo = sudoku_io()
numRead = myIo.readFile("sudoku_1.txt")
suText, suComment = myIo.getSudokuList()

# now create a sudoku class and provide SUDOKU to that class
mySudoku = sudoku_np1()

if SU_NUM_ALL:
    SU_NUM_START=0
    SU_NUM_STOP=numRead

for i in range(SU_NUM_START,SU_NUM_STOP):
    # set the sudoku by providing it in string/text form
    mySudoku.setSuArray(suText[i])
    mySudoku.setComment(suComment[i])
    # print the unsolved SUDOKU
    if PRINT_FLAG:
        print(f"\nInput SUDOKU array #{i}")
        mySudoku.print(True)

    # now call a solver method
    solved = mySudoku.solver1(False)
    # if solver1 does not succeed, call solver2
    if solved:
        print(f"\n=====> PASS: Solved SUDOKU #{i} with solver1")
        if mySudoku.checkSudokuIsValid()==False:
            print(f"\n=====> ERROR in solution for SUDOKU array #{i}: SUDOKU is not valid")
    if not solved and USE_SOLVER2:
        solved, num_guesses = mySudoku.solver2(MAX_GUESS_NUM)
        if solved:
            if mySudoku.checkSudokuIsValid()==False:
                print(f"\n=====> ERROR in solution for SUDOKU array #{i}: SUDOKU is not valid",end="")
                solved=False
            else:
                print(f"\n=====> PASS: Solved SUDOKU #{i} with solver2")
 
    
    if not solved:
            print(f"\n=====> FAIL: No solution found for SUDOKU #{i} with selected solver algorithms")
            mySudoku.printAllCandidateList()
    # finally check if the solution is valied

    # print the solved SUDOKU
    if PRINT_FLAG:
        mySudoku.checkSudokuIsValid()
        print(f"\nSolution SUDOKU array for #{i}")
        mySudoku.print(True)