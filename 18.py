def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            val = 0
            for k in range(len(matrix2)):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)
    return result


def get_matrix_from_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    print("Resultant Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))


matrix1 = [[1, 1], [1, 1]]
matrix2 = [[1, 1], [1, 2]]

result = multiply_matrices(matrix1, matrix2)
print_matrix(result)