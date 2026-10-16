from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    dq = deque(map(int, input().split()))
    last = float('inf')
    for _ in range(n):
        if dq[0] >= dq[-1]:
            cur = dq.popleft()
        else:
            cur = dq.pop()
        if cur > last:
            print("No")
            break
        last = cur
    else:
        print("Yes")
