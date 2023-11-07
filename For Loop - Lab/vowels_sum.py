#Read user input

my_string = input()

total = 0
#Logic

for i in range(0, len(my_string)):
    char = my_string[i]

    if char == 'a':
        total += 1
    elif char == 'e':
        total += 2
    elif char == 'i':
        total += 3
    elif char == 'o':
        total += 4
    elif char == 'u':
        total += 5

#Output

print(total)