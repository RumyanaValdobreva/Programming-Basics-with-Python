#Read user input

product_name = input()

#Logic

result = ''

if product_name == 'banana' or product_name == 'apple' or product_name == 'kiwi' or product_name == 'cherry' or product_name == 'lemon' or product_name == 'grapes':
    result = 'fruit'
elif product_name == 'tomato' or product_name == 'cucumber' or product_name == 'pepper' or product_name == 'carrot':
    result = 'vegetable'
else:
    result = 'unknown'

#Output

print(result)