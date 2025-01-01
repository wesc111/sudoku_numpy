# SUDOKU makefile
# WSC, 1-Jan-2025

NUM=1

help:
	@echo "make pydoc                   ... generate pydoc documentation for sudoku_np1 class"
	@echo "make solve                   ... solve SUDOKU #1 by running sudoku.py"
	@echo "make solve NUM=13            ... solve SUDOKU #13"
	@echo "make solve START=10 STOP=20  ... solve SUDOKUs from #10 to #20"

.PHONY: pydoc

solve:
	python3 sudoku.py -num=$(NUM)

pydoc: sudoku_np1.py
	python3 -m pydoc -w sudoku_np1
	cp sudoku_np1.html doc/_static
