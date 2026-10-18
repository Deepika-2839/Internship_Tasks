
# Number of students subscribed to English
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French
m = int(input())
french = set(map(int, input().split()))

# Combine both sets (duplicate roll numbers are counted once)
all_students = english.union(french)

# Print the total number of students
print(len(all_students))
