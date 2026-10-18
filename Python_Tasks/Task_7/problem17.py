
def separateNumbers(s):
    # A beautiful string must contain at least 2 numbers
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    # Try different lengths for the first number
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        expected = first
        result = str(first)

        # Build the sequence until it reaches the string length
        while len(result) < len(s):
            expected += 1
            result += str(expected)

        # Check whether the generated sequence matches the input
        if result == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
