if __name__ == '__main__':
    n = int(input())
    students = []

    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find all unique scores sorted
    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    # Get names with second lowest score and sort alphabetically
    result = sorted([name for name, score in students if score == second_lowest])

    for name in result:
        print(name)
