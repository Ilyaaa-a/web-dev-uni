N = int(input().strip())

count = [0] * 60 * 24 * 2

for i in range(N):
    passanger = input().strip().split()
    in_time = int(passanger[0])
    out_time = int(passanger[1])

    for j in range(in_time, out_time+1):
        count[j] += 1

T = int(input().strip())
    
print(count[T])