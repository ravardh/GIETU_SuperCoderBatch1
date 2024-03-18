m, n = map(int, input("Enter the number of rows and columns of the 1st matrix: ").split())
p, q = map(int, input("Enter the number of rows and columns of the 2nd matrix: ").split())

if n != p:
    print("Multiplication not possible, exiting.")
    exit()

print("Enter the elements of the first matrix:")
a = [[int(input()) for _ in range(n)] for _ in range(m)]

print("Enter the elements of the second matrix:")
b = [[int(input()) for _ in range(q)] for _ in range(p)]

print("Multiplied matrix:")
c = [[0] * q for _ in range(m)]

for i in range(m):
    for j in range(q):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]

for i in range(m):
    for j in range(q):
        print(c[i][j], end='\t')
    print()
