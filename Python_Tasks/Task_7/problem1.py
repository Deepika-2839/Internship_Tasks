
# Number of students subscribed to English
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French
m = int(input())
french = set(map(int, input().split()))

# Find students subscribed to only one newspaper
result = english.symmetric_difference(french)

# Print the total number of students
print(len(result))
