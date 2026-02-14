s = input().strip()

arr = s.split()

res = ''

for i in range(len(arr)):
    if (i != len(arr) - 1):
        res += (arr[i] + '-')
    else:
        res += arr[i]

print(res)