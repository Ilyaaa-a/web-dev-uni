N = int(input().strip())

if (2 <= N <= 5):

    people = []
    all_scores = set()

    for i in range(N):
        name = input().strip()
        score = float(input().strip())

        people.append([name, score])
        all_scores.add(score)

    all_scores_list = sorted(all_scores)

    second_score = all_scores_list[1]

    names = []
    for name, score in people:
        if score == second_score:
            names.append(name)

    names.sort()

    for name in names:
        print(name)

else: print('Error')




