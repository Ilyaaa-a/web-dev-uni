n = int(input().strip())
A = list(map(int, input().split(' ')))

unique_scores = sorted(set(A), reverse=True)

print(unique_scores[1])