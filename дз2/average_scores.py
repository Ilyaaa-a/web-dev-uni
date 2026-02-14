def compute_average_scores(scores):
    if not scores:
        return ()
    
    subjects = [list(subject) for subject in scores]
    X = len(subjects) 
    N = len(subjects[0]) 
    
    if not (0 < N <= 100): return "Error"
    if not (0 < X <= 100): return "Error"
        

    for subj in subjects:
        if len(subj) != N:
            return "Error"
        
    for subject in subjects:
        for score in subject:
            if not (0 <= score <= 100):
                return "Error"

    averages = []
    for student_index in range(N):
        total = 0.0
        for subject in subjects:
            total += subject[student_index]
        average = total / X
        
        averages.append(round(average, 1))
    
    return tuple(averages)


if __name__ == "__main__":
    scores_example = [
        (89, 90, 78, 93, 80),
        (90, 91, 85, 88, 86),
        (91, 92, 83, 89, 90.5)
    ]
    result = compute_average_scores(scores_example)
    for avg in result:
        print(f"{avg:.1f}")

# compute_average_scores()

# def compute_average_scores():
#     N, X = input().split(" ")
#     N = int(N)
#     X = int(X)

#     scores = []

#     for i in range(X):
#         scores.append(list(map(float, input().split())))

#     for i in range(N):
#         total = 0
#         for subject_scores in scores:
#             total += subject_scores[i]  # оценка студента по этому предмету
#         average = total / X
#         print(f"{average:.1f}")

# compute_average_scores()