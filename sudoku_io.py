# sudoku_io sudoku class
# SUDOKU IO class for input/output functions in sudoku
# Version 0.00, WSC, 7-Nov-2024

import numpy as np
import re

class sudoku_io:
    suText=[]
    suComment=[]

    def readFile(self, fileName):
        i=0
        fp = open(fileName,"r")
        for elem in fp:
            elem = re.sub(r" *\/\/ *","//",elem)
            elem = elem.replace("\n","")
            if elem=="STOP":
                print(f"sudoku_io: found STOP on line {i}, stopping file read there (skipping lines after STOP)")
                break
            lineTokens = elem.split("//")
            suStr=lineTokens[0]
            if len(lineTokens)>1:
                comStr=lineTokens[1]
            if len(suStr)==81:
                self.suText.append(suStr)
                self.suComment.append(comStr)
                i+=1
        print(f"sudoku_io: Total of {i} lines read from file {fileName}")
 
    def getSudokuList(self):
        return self.suText, self.suComment