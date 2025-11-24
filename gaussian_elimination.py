def gaussian_elimination_ref(a):
    n = len(a)

    for i in range(n):
        # If pivot is zero, swap with a row below
        if a[i][i] == 0:
            for k in range(i + 1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    break

        # Eliminate entries below pivot
        for j in range(i + 1, n):
            if a[i][i] == 0:
                continue
            ratio = a[j][i] / a[i][i]
            for k in range(i, len(a[0])):
                a[j][k] = a[j][k] - ratio * a[i][k]

    return a


# --- User Input ---
n = int(input("Enter number of equations (rows): "))
m = int(input("Enter number of variables + 1 (columns in augmented matrix): "))

print("Enter the augmented matrix row by row:")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

# Perform Gaussian Elimination
ref = gaussian_elimination_ref(A)

# Display Result
print("\nRow Echelon Form (REF):")
for row in ref:
    print([round(x, 3) for x in row])

''' Enter number of equations (rows): 3
Enter number of variables + 1 (columns in augmented matrix): 4
Enter the augmented matrix row by row:
Row 1: 1 2 1 7
Row 2: 2 3 3 18
Row 3: 0 1 2 8

Row Echelon Form (REF):
[1.0, 2.0, 1.0, 7.0]
[0.0, -1.0, 1.0, 4.0]
[0.0, 0.0, 3.0, 12.0]
'''
