# Delete nth Column for Cofactor
def delete_nth_column_helper(matrix, n):

    return [m[:n]+m[n+1:] for m in matrix[1:]]

# Calculate Matrix Determinant
def determinant(matrix):
    
    # Base Cases
    if len(matrix) == 1: return matrix[0][0]
    if len(matrix) == 2: return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    # Calculate Determinant Parts
    for _ in range(len(matrix[0])): 

        determinant_components = [(-1)**i*matrix[0][i]*determinant(delete_nth_column_helper(matrix, i)) for i in range(len(matrix[0]))]

    # Return Sum
    return sum(determinant_components)

if __name__ == "__main__":

    matrix = []
    
    # Get Matrix
    for _ in range(int(input())): matrix.append([int(i) for i in input().split()])

    # Output
    print(determinant(matrix))