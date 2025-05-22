# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. 
# However, we encountered an issue, as whenever we change a value in one nested list, 
# all nested lists are affected. Can you fix the code?

from copy import deepcopy

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(deepcopy(sub_list))

matrix[0][0] = "X"
print(matrix)

# Originally did not copy the 'sub_list' variable

# LS solution
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy()) # Utilizes the built-in 'copy()' method.

matrix[0][0] = "X"
print(matrix)