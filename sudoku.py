# numpy example
# WSC, 27-Oct-2024

# read a string representing a 9x9 SUDOKU into a numpy array

from sudoku_np1 import sudoku

suText=[]
suComment=[]

suText.append("8.534...12.4...59..1...5.686...83....9361....7...52....5...8.421.7...68.4.219...5")
suComment.append("kleinezeitung, 14.09.2020 - leicht")

suText.append("4.8..6.13.7..89.252.6.7...........72.24...39.83...........4.5.758.69..4.34.2..9.8")
suComment.append("kleinezeitung, 17.09.2020 - leicht")

suText.append("9..25.8.1.....82..18.39.....9..3.7.56.37.19.44.7.8..3.....13.68..15.....3.5.72..9")
suComment.append("kleinezeitung, 22.10.2020 - leicht")

suText.append("9157.3....86.....33....2.69.3...4.1.74.9.5.28.5.8...4.19.2....64.....57....1.7892")
suComment.append("kleinezeitung, 08.12.2020 - leicht")

suText.append("8.534...12.4...59..1...5.686...83....9361....7...52....5...8.421.7...68.4.219...5")
suComment.append("kleinezeitung, 14.09.2020 - leicht")

suText.append(".319..7458....7.61....3...2....1.2.424.6.5.399.7.4....3...8....18.7....6472..198.")
suComment.append("kleinezeitung, 02.01.2021 - leicht")

suText.append("..1.3.2....37284.....6.9......162...13.....89.7.....4.....7....78.....64.5.8.4.2.")
suComment.append("kleinezeitung, 18.09.2020 - mittel")

suText.append(".....35..35.........4...8.3..193...4.89.54......7.6...8...627..4...8..3.196....5.")
suComment.append("kleinezeitung, 21.10.2020 - mittel")

suText.append(".....6.2.615...74..9.7...8.9...7.2.....4.8.....7.9...3.3...7.6..61...875.2.1.....")
suComment.append("kleinezeitung, 24.10.2020 - mittel")

suText.append(".3..259..87...62.4......7.......4...6...73.2929.16....312...8......1..9..8..5...2")
suComment.append("kleinezeitung, 23.10.2020 - mittel")

suText.append("..3...8...8..3..5.5..8.9..6..79.25...9..7..2...16.54..1..7.4..3.5..1..8...6...7..")
suComment.append("kleinezeitung, 05.12.2020 - mittel")

suText.append("....4..69.4...3....98.2.74.5..4.7.....9.3..8.1..2.8....13.5.49..7...4.......8..32")
suComment.append("kleinezeitung, 31.12.2020 - mittel")

suText.append(".1.....2....512...2..8.6..55.8...3.1.6.4.9.7.73.....42..3...7....6.7.2.....3.5...")
suComment.append("kleinezeitung, 04.01.2021 - mittel")

suText.append("1......687.9.3......86..13.....8.3...4.3.1.8...7.2.....14..35......4.8.995......3")
suComment.append("kleinezeitung, 05.01.2021 - mittel")

# the number of the sudoku that should be tested
TEST_SUDOKU_NUM = 10

PRINT_SUDOKU = True
TEST_SUDOKU_FUNC = False
TEST_SUDOKU_CAND = False
TEST_SUDOKU_SOLVER1 = True

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
        for row in range(0,9):
            for col in range(0,9):
                mySudoku.printCandidateList(row,col)

    # run solver just with solveSingles() algorithm
    if TEST_SUDOKU_SOLVER1:
        i=0
        n=1
        while (n>0):
            n = mySudoku.solveSingles()
            print(f"i={i}: num solved singles = {n}")
            i+=1
        mySudoku.print()
        if mySudoku.checkSolved():
            print(f"SUCCESS: Sudoku is solved with SOLVER1")
        else:
            print(f"FAIL:    No Sudoku solution found with SOLVER1")
