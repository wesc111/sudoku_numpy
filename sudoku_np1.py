# sudoku_np1 sudoku class
# SUDOKU based on numpy
# Version 0.0, WSC, 27-Oct-2024

import numpy as np
from enum import Enum

# define element type
class suElemT(Enum):
    UNDEFINED = 0
    FIXED = 1
    SOLVED_SINGLE = 2
    

# python class to solve SUDOKUs in a human way (without backtracking)
class sudoku:

    def __init__(self):
        self.suArray = np.zeros((9,9), dtype=np.int8)
        self.suArrayType = np.zeros((9,9), dtype=suElemT)
        self.comment = ""

    def setComment(self,string):
        self.comment = string

    def setSuArray(self,suText):
        row=col=0
        for elem in suText:
            if elem=='.' or elem=='0':
                elem='0'
                self.suArrayType[row][col] = suElemT.UNDEFINED
                self.suArray[row][col] = int(elem)
            else:
                self.suArrayType[row][col] = suElemT.FIXED
                self.suArray[row][col] = int(elem)
            if col==8:
                col=0
                if row<8:
                    row+=1
                else:
                    break
            else:
                col+=1

    def getSuArray(self):
        return self.suArray
    
    def getValListInRow(self,num):
        valList = []
        for i in range(0, 9):
            aVal=self.suArray[num][i]
            if aVal>0:
                valList.append(aVal) 
        valList.sort()
        return valList 
    
    def printValListInRow(self, num):
        ll = self.getValListInRow(num)
        print(f"row   #{num}: ",end='')
        for e in ll:
            print(f"{e},",end='')
        print(" ")

    def getValListInCol(self,num):
        valList = []
        for i in range(0, 9):
            aVal=self.suArray[i][num]
            if aVal>0:
                valList.append(aVal) 
        valList.sort()
        return valList 
    
    def printValListInCol(self, num):
        ll = self.getValListInCol(num)
        print(f"col   #{num}: ",end='')
        for e in ll:
            print(f"{e},",end='')
        print(" ")

    # get the block number of element defined by row, col
    def getBlockNum(self,row,col):
        return int(col/3) + 3*int(row/3)

    def getValListInBlock(self,blocknum):
        valList = []
        for row in range(0, 3):
            cOffset = 3 * (blocknum % 3)
            rOffset = 3 * int(blocknum / 3)
            for col in range(0,3):
                aVal=self.suArray[row+rOffset][col+cOffset]
                if aVal>0:
                    valList.append(aVal)
        valList.sort()
        return valList
    
    def printValListInBlock(self,num):
        ll = self.getValListInBlock(num)
        print(f"block #{num}: ",end='')
        for e in ll:
            print(f"{e},",end='')
        print(" ")

    def getCandidateList(self,row,col):
        candidateList = [1,2,3,4,5,6,7,8,9]
        for e in self.getValListInRow(row):
            if e in candidateList:
                candidateList.remove(e)
        for e in self.getValListInCol(col):
            if e in candidateList:
                candidateList.remove(e)
        for e in self.getValListInBlock(self.getBlockNum(row,col)):
            if e in candidateList:
                candidateList.remove(e)
        return candidateList
    
    def printCandidateList(self,row,col):
        if self.suArrayType[row][col] == suElemT.UNDEFINED:
            ll = self.getCandidateList(row,col)
            print(f"candidates row={row}, col={col}: ",end='')
            for e in ll:
                print(f"{e},",end='')
            print(" ")

    def checkSolved(self):
        solvedFlag = True
        for row in range(0,9):
            for col in range(0,9):
                if self.suArrayType[row][col] == suElemT.UNDEFINED:
                    solvedFlag = False
        return solvedFlag

    def solveSingles(self):
        numSolvedSinglesFound = 0
        for row in range(0,9):
            for col in range(0,9):
                if self.suArrayType[row][col] == suElemT.UNDEFINED:
                    ll = self.getCandidateList(row,col)
                    if len(ll)==1:
                        self.suArrayType[row][col] = suElemT.SOLVED_SINGLE
                        self.suArray[row][col] = int(ll[0])
                        numSolvedSinglesFound+=1
        return numSolvedSinglesFound

    def findLonePairs(self):
        # TBD
        return False

    def print(self):
        print(self.suArray)
    def printComment(self):
        print(f"===== {self.comment}")