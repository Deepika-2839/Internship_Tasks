def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        middle = alphabet[size - i - 1]
        right = left[::-1]
        letters = left + middle + right
        row = "-".join(letters)
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines + lines[-2::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
