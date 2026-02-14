N = int(input().strip());

if N < 1 or N > 100:
    print('Error')
elif N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and 2<=N<=5:
    print("Not Weird")
elif N % 2 == 0 and 6<=N<=20:
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")
