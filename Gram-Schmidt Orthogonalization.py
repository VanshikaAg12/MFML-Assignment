import math

def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))

def subtract(u, v):
    return [ui - vi for ui, vi in zip(u, v)]

def scalar_multiply(c, v):
    return [c * vi for vi in v]

def norm(v):
    return math.sqrt(dot(v, v))

def transpose(A):
    return [list(col) for col in zip(*A)]

def gram_schmidt(A):
    A = transpose(A)  # work with columns
    orthogonal = []
    for v in A:
        for u in orthogonal:
            proj_coeff = dot(v, u) / dot(u, u)
            v = subtract(v, scalar_multiply(proj_coeff, u))
        orthogonal.append(v)

    # Normalize to get orthonormal vectors
    orthonormal = []
    for v in orthogonal:
        v_norm = norm(v)
        if v_norm == 0:
            print("Matrix has linearly dependent columns!")
            return None
        orthonormal.append([vi / v_norm for vi in v])

    return transpose(orthonormal)

# --- User Input ---
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
print("Enter the matrix row by row:")
A = [list(map(float, input().split())) for _ in range(n)]

# Perform Gram-Schmidt
Q = gram_schmidt(A)

if Q:
    print("\nOrthonormal Matrix (Q):")
    for row in Q:
        print([round(x, 3) for x in row])

'''Enter number of rows: 2
Enter number of columns: 2
Enter the matrix row by row:
2 1
-1 1

Orthonormal Matrix (Q):
[0.894, 0.447]
[-0.447, 0.894]'''
