# Read user input

day = input()

# Logic

result = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    result = 12
elif day == 'Wednesday' or day == 'Thursday':
    result = 14
else:
    result = 16

# Output

print(result)