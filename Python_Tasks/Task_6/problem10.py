
n, m = map(int, input().split())

# Print the upper half of the mat
for i in range(1, n, 2):
    print(('.|.' * i).center(m, '-'))

# Print WELCOME in the center
print('WELCOME'.center(m, '-'))

# Print the lower half of the mat
for i in range(n - 2, 0, -2):
    print(('.|.' * i).center(m, '-'))
