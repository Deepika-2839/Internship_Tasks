from collections import Counter

if __name__ == '__main__':
    X = int(input())
    sizes = list(map(int, input().split()))

    shoe_counter = Counter(sizes)

    N = int(input())
    total_earned = 0

    for _ in range(N):
        size, price = map(int, input().split())
        if shoe_counter[size] > 0:
            total_earned += price
            shoe_counter[size] -= 1

    print(total_earned)
