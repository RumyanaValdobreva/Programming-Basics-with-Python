n = int(input())
odd_sum = 0
even_sum = 0

for i in range(0, n):
    user_input = int(input())
    if i % 2 == 0:
        odd_sum += user_input
    else:
        even_sum += user_input

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {even_sum}')

else:
    print('No')
    print(f'Diff = {abs(odd_sum - even_sum)}')