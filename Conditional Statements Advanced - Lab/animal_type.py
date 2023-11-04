# Read user input

animal = input()
result = ''

# Logic

if animal == 'dog':
    result = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    result = 'reptile'
else:
    result = 'unknown'

# Output
print(result)