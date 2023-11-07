# Read user input
min_number = int(input())

# Logic
while True:
    user_input = input()
    if user_input == 'Stop':
        break
    user_input = int(user_input)
    if user_input < min_number:
        min_number = user_input

# Output
print(min_number)