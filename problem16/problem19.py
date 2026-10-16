# Problem: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
n = int(input())
sizes = Counter(map(int, input().split()))
customers = int(input())
income = 0
for _ in range(customers):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        income += price
        sizes[size] -= 1
print(income)
