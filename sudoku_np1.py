# sudoku_np1 sudoku class
# SUDOKU based on numpy
# Version 0.0, WSC, 5-Nov-2024

import numpy as np
from enum import Enum

import time

# Class suElemT defines the type of a Sudoku element
class suElemT(Enum):
    UNDEFINED = 0
    FIXED = 1
    SOLVED_SINGLE = 2
    SOLVED_HIDDEN_SINGLE = 3

# The candidate list for a sudoku element
class candidateList():
    row = 0
    col = 0
    block = 0
    list = []
    def print(self):
        print(f"row={self.row}, col={self.col} block={self.block}: {self.list}")

# python class to solve SUDOKUs in a human way (without backtracking)
class sudoku:
    def __init__(self):
        self.suArray = np.zeros((9,9), dtype=np.int8)
        self.suArrayType = np.zeros((9,9), dtype=suElemT)

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
        self.calcAllCandidateList()

    def getSuArray(self):
        return self.suArray
    
    # central calculation of the self.allCandidateList
    def calcAllCandidateList(self):
        self.allCandidateList = []
        for row in range(0,9):
            for col in range(0,9):
                if self.suArrayType[row][col] == suElemT.UNDEFINED:
                    cl = candidateList()
                    cl.row = row
                    cl.col = col
                    cl.block = self.getBlockNum(row,col)
                    cl.list = self.calcCandidateList(row,col)
                    self.allCandidateList.append(cl)  

    # calculate the candidate list for specific cell at row, col
    def calcCandidateList(self,row,col):
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
    
    # get the candidates of specific row, col
    def getCandidateList(self,row,col):
        for elem in self.allCandidateList:
            if elem.row==row and elem.col==col:
                return elem.list
        return []
    
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
  
    # print the actual list of all candidates
    # note that the candidates need to be calculated before, eg with calcAllCandidateList()
    def printAllCandidateList(self):
        print("List of all candidates in actual sudoku:")
        for elem in self.allCandidateList:
            elem.print()

    def checkSolved(self):
        solvedFlag = True
        for row in range(0,9):
            for col in range(0,9):
                if self.suArrayType[row][col] == suElemT.UNDEFINED:
                    solvedFlag = False
        return solvedFlag
    
    def solveSingles(self):
        numSolvedSinglesFound = 0
        self.calcAllCandidateList()
        for elem in self.allCandidateList:
            row = elem.row
            col = elem.col
            if self.suArrayType[row][col] == suElemT.UNDEFINED and len(elem.list)==1:
                self.suArrayType[row][col] = suElemT.SOLVED_SINGLE
                self.suArray[row][col] = int(elem.list[0])
                numSolvedSinglesFound+=1
        return numSolvedSinglesFound

    def findLonePairs(self):
        # TBD, not finished now
        # i=0...row, 1...col, 2...block
        for i in range(0,2):
            for j in (range(0,9)):
                ddList=[]
                # iterate through all elements
                for elem in self.allCandidateList:
                    if (i==0 and elem.row==j) or (i==1 and elem.col==j) or (i==2 and elem.block==j):
                        if len(elem.list)==2:
                            ddList.append(elem.list)
                if len(ddList)>1:
                    dupFlag, dup = self.checkDuplicates(ddList)
                    if dupFlag:
                        if i==0:
                            print(f"LONE row={j}:  {dupFlag}, {dup}, {ddList}")
                        if i==1:
                            print(f"LONE col={j}:  {dupFlag}, {dup}, {ddList}")
                        if i==2:
                            print(f"LONE block={j}: {dupFlag}, {dup}, {ddList}")
        return False
    
    # find singles in the input list cc
    def findSingle(self, cc):
        oc = [0,0,0,0,0,0,0,0,0,0]
        for elem in cc:
            oc[elem] += 1
        retVal = []
        count = 0
        for i in range(1,9):
            if oc[i]==1:
                retVal.append(i)
                count += 1
        return count, retVal
    
    # solve hidden singles
    # hidden singles are elements that appear just once in a row, col or block list
    def solveHiddenSingles(self,debug=False):
        self.calcAllCandidateList()
        hiddenSinglesFound = 0
        for row in range(0,9):
            cc = []
            # create list cc with all elements inside of row
            for col in (range(0,9)):
                for elem in  self.getCandidateList(row,col):
                    cc.append(elem)
            cc.sort()
            count, hsList = self.findSingle(cc)
            if count>0:
                if (debug):
                    print(f"Found hidden singles {hsList} in row {row}")
                self.setHiddenSingles(0, row, hsList)
                hiddenSinglesFound += len(hsList)
        for col in range(0,9):
            cc = []
            # create list cc with all elements inside of col
            for row in (range(0,9)):
                for elem in  self.getCandidateList(row,col):
                    cc.append(elem)
            cc.sort()
            count, hsList = self.findSingle(cc)
            if count>0:
                if (debug):
                    print(f"Found hidden singles {hsList} in col {col}")
                self.setHiddenSingles(1, col, hsList)
                hiddenSinglesFound += len(hsList)
        for block in range(0,9):
            cc = []
            # create list cc with all elements inside of block
            for blockElem in self.blockIndexList(block):
                row, col = blockElem
                for elem in  self.getCandidateList(row,col):
                    cc.append(elem)
            cc.sort()
            count, hsList = self.findSingle(cc)
            if count>0:
                if (debug):
                    print(f"Found hidden singles {hsList} in block {block}")
                self.setHiddenSingles(2, block, hsList)
                hiddenSinglesFound += len(hsList)
        
        return hiddenSinglesFound
    
    # return a list of row,col indices for a block number
    def blockIndexList(self,block):
        if   block==0: 
            return [[0,0],[0,1],[0,2], [1,0],[1,1],[1,2], [2,0],[2,1],[2,2]]
        elif block==1: 
            return [[0,3],[0,4],[0,5], [1,3],[1,4],[1,5], [2,3],[2,4],[2,5]]
        elif block==2: 
            return [[0,6],[0,7],[0,8], [1,6],[1,7],[1,8], [2,6],[2,7],[2,8]]
 
        elif block==3: 
            return [[3,0],[3,1],[3,2], [4,0],[4,1],[4,2], [5,0],[5,1],[5,2]]
        elif block==4: 
            return [[3,3],[3,4],[3,5], [4,3],[4,4],[4,5], [5,3],[5,4],[5,5]]
        elif block==5: 
            return [[3,6],[3,7],[3,8], [4,6],[4,7],[4,8], [5,6],[5,7],[5,8]]
 
        elif block==6: 
            return [[6,0],[6,1],[6,2], [7,0],[7,1],[7,2], [8,0],[8,1],[8,2]]
        elif block==7: 
            return [[6,3],[6,4],[6,5], [7,3],[7,4],[7,5], [8,3],[8,4],[8,5]]
        elif block==8: 
            return [[6,6],[6,7],[6,8], [7,6],[7,7],[7,8], [8,6],[8,7],[8,8]]        
 
        else:           
            return [[0,0],[0,0],[0,0], [0,0],[0,0],[0,0], [0,0],[0,0],[0,0]]       
    # return a list of indices for a row
    def rowIndexList(self,row):
       return [[row,0],[row,1],[row,2], [row,3],[row,4],[row,5], [row,6],[row,7],[row,8]]
    # return a list of indices for a column
    def colIndexList(self,col):
       return [[0,col],[1,col],[2,col], [3,col],[4,col],[5,col], [6,col],[7,col],[8,col]]

    # type: row=0, col=1, block=2
    # num ... row/block/col number (0-8)
    # singleList ... list of hidden singles (found with findHiddenSingles)
    def setHiddenSingles(self, type, num, singleList):
        if type==0:
            for elem in singleList:
                row = num
                for col in range(0,9):
                    if self.suArray[row,col]==0 and elem in self.getCandidateList(row,col):
                        self.suArray[row,col] = elem
                        self.suArrayType[row,col] = suElemT.SOLVED_HIDDEN_SINGLE
        elif type==1:
            for elem in singleList:
                col = num
                for row in range(0,9):
                    if self.suArray[row,col]==0 and elem in self.getCandidateList(row,col):
                        self.suArray[row,col] = elem
                        self.suArrayType[row,col] = suElemT.SOLVED_HIDDEN_SINGLE
        elif type==2:
            for elem in singleList:
                block = num
                for blockElem in self.blockIndexList(block):
                    row, col = blockElem
                    if self.suArray[row,col]==0 and elem in self.getCandidateList(row,col):
                        self.suArray[row,col] = elem
                        self.suArrayType[row,col] = suElemT.SOLVED_HIDDEN_SINGLE

    # check if there are duplicates in the list ll
    def checkDuplicates(self, ll):
        for i in range(0,len(ll)):
            for j in range(0,len(ll)):
                if i!=j:
                    if ll[i]==ll[j]:
                        return True, ll[i]
        return False, [0,0]

    def solver1(self, debug=False):
        startTime = time.time()
        i=m=0
        n=1
        while n>0 or m>0 or i<20:
            n = self.solveSingles()
            self.calcAllCandidateList()
            m = self.solveHiddenSingles(debug)
            if debug and (n>0 or m>0):
                print(f"i={i}: ",end="")
            if debug and n>0:
                print(f"num solved singles = {n} ",end="")
            if debug and m>0:
                print(f", num solved hidden singles = {m}",end="")
            if debug and (n>0 or m>0):
                print("")
            i+=1
        endTime =time.time()
        if self.checkSolved():
            print(f"SUCCESS: Sudoku is solved with SOLVER1, elapsed time is {endTime-startTime:.3f}")
            return True
        else:
            if debug:
                for elem in self.allCandidateList:
                    elem.print()
            print(f"FAIL:    No Sudoku solution found with SOLVER1, elapsed time is {endTime-startTime:.3f}")
            return False

    # print the sudoku array
    # TBD: pretty print should be added 
    def print(self):
        print(self.suArray)
    # print the comment
    # just for information
    def printComment(self):
        print(f"===== {self.comment}")