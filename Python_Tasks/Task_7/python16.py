
def caesarCipher(s, k):
    result = ""

    # Reduce k because the alphabet has only 26 letters
    k = k % 26

    for char in s:
        if char.islower():
            # Shift lowercase letters
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result += new_char

        elif char.isupper():
            # Shift uppercase letters
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result += new_char

        else:
            # Keep symbols and numbers unchanged
            result += char

    return result


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)
