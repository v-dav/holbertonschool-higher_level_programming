def square_matrix_simple(matrix=[]):
    if matrix != []:
        new_list = [list(map(lambda x: x ** 2, sublist)) for sublist in matrix]
        return new_list
