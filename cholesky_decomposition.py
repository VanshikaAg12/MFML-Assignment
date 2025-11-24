import math

def is_symmetric(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True

def cholesky_decomposition(a):
    n = len(a)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_val = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:  # Diagonal elements
                val = a[i][i] - sum_val
                if val <= 0:
                    print("Matrix is not positive definite.")
                    return None
                L[i][j] = math.sqrt(val)
            else:  # Off-diagonal elements
                if L[j][j] == 0:
                    print("Matrix is not positive definite.")
                    return None
                L[i][j] = (a[i][j] - sum_val) / L[j][j]

    return L

# --- User Input ---
n = int(input("Enter the order of the matrix: "))
print("Enter the matrix row by row:")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

# --- Check symmetry ---
if not is_symmetric(A):
    print("\nMatrix is not symmetric. Cholesky decomposition not possible.")
else:
    L = cholesky_decomposition(A)
    if L:
        print("\nLower Triangular Matrix L:")
        for row in L:
            print([round(x, 3) for x in row])
'''Enter the order of the matrix: 3
Enter the matrix row by row:
Row 1: 4 12 -16
Row 2: 12 37 -43
Row 3: -16 -43 98

Lower Triangular Matrix L:
[2.0, 0.0, 0.0]
[6.0, 1.0, 0.0]
[-8.0, 5.0, 3.0]'''
