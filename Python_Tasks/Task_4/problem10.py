# Problem: Finding the percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

query_name = input()
marks = student_marks[query_name]
avg = sum(marks) / len(marks)
print(f"{avg:.2f}")
