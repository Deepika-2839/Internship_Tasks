# Problem: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    
    # Symmetric difference = (a-b) U (b-a)
    result = sorted(a.symmetric_difference(b))
    
    for i in result:
        print(i)
