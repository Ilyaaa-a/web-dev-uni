a = int(input().strip())
b = int(input().strip())

if (1 <= a <= 10**10) and (1 <= b <= 10**10):
    print(a+b)
    print(a-b)
    print(a*b)
else:
    print('Error')

