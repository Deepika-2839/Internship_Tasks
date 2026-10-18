
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French
m = int(input())
french = set(map(int, input().split()))

# Find students subscribed only to English
only_english = english.difference(french)

# Print the total number of students
print(len(only_english))
