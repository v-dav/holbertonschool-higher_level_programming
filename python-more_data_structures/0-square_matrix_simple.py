def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append([])  # Ajouter une nouvelle sous-liste pour chaque sous-liste dans matrix
            for j in range(len(matrix[i])):
                new_matrix[i].append(matrix[i][j] ** 2)  # Ajouter le carré de la valeur à la sous-liste appropriée
        return new_matrix
    else:
        return matrix  # Si matrix est vide ou None, retourner matrix
