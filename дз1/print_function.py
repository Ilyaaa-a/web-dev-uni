n = int(input().strip())

if (1 <= n <= 20):
    for i in range(n+1):
        print(i, end='')
else: print('Error')