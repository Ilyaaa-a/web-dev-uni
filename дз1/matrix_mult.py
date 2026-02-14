n = int(input())

A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# матрица для результата
C = [[0] * n for _ in range(n)]

# умножение
for i in range(n):
    for j in range(n):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        C[i][j] = total


for i in range(n):
    print(' '.join(map(str, C[i])))