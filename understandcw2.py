import numpy.random as random
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid7 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]

def check_section(section, n):

	if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
		return True
	return False


def get_squares(grid, n_rows, n_cols):

	squares = []
	for i in range(n_cols):
		rows = (i*n_rows, (i+1)*n_rows)
		for j in range(n_rows):
			cols = (j*n_cols, (j+1)*n_cols)
			square = []
			for k in range(rows[0], rows[1]):
				line = grid[k][cols[0]:cols[1]]
				square +=line
			squares.append(square)


	return(squares)


def check_solution(grid, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	n = n_rows*n_cols

	for row in grid:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows):
		column = []
		for row in grid:
			column.append(row[i])
		if check_section(column, n) == False:
			return False

	squares = get_squares(grid, n_rows, n_cols)
	for square in squares:
		if check_section(square, n) == False:
			return False

	return True


def random_solve(grid, n_rows, n_cols, max_tries=500):
	for i in range(max_tries):
		temporary=grid
		my_list = [m for m in range(1, n_rows + 1)]
		n = n_rows * n_cols
		for i in range(n_rows):
			for k in range(n_cols):
				if temporary[i][k] == 0:
					temporary[i][k] = random.choice(my_list)
				if check_solution(temporary,n_rows,n_cols)==True:
					return temporary

	#
	# 	pass
	#
	# return grid


# def solve(grid, n_rows, n_cols):
# 	'''
# 	Solve function for Sudoku coursework.
# 	Comment out one of the lines below to either use the random or recursive solver
# 	'''
#
# 	return random_solve(grid, n_rows, n_cols)
# 	# return recursive_solve(grid, n_rows, n_col

def find_zero(grid,n_rows,n_cols):
	my_list=[m for m in range (1,n_rows+1)]
	n = n_rows*n_cols
	for i in range(n_rows):
		for k in range(n_cols):
			if grid[i][k]==0:
				grid[i][k]=random.choice(my_list)
	return grid

def solve(grid, n_rows, n_cols):
	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''
	newgrid=find_zero(grid,n_rows,n_cols)
	check=check_solution(newgrid,n_rows,n_cols)
	return grid,check

	# return random_solve(grid, n_rows, n_cols)
	# return recursive_solve(grid, n_rows, n_col






print(random_solve(grid3,4,4))





