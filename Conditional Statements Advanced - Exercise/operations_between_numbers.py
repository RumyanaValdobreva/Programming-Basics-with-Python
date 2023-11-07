number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0
if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'

    print(f'{number_1} {operator} {number_2} = {result} - {type_number}')

elif operator == '/' and number_2 != 0:
    print(f'{number_1} / {number_2} = {number_1 / number_2:.2f}')
elif operator == '%' and number_2 != 0:
    print(f'{number_1} % {number_2} = {number_1 % number_2}')

if number_2 == 0:
    print(f'Cannot divide {number_1} by zero')