# Read input

age = float(input())
gender = str(input())
result = ''

# Logic

if gender == 'm':
    if age >= 16:
        result = 'Mr.'
    else:
        result = 'Master'
elif gender == 'f':
    if age >= 16:
        result = 'Ms.'
    else:
        result = 'Miss'

# Output

print(result)