# Problem: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))
result = sorted(a.symmetric_difference(b))
for i in result:
    print(i)
