number = int(input())

total_bonus = 0

if number <= 100:
    total_bonus += 5
if 100 < number < 1000:
    total_bonus += number * 20/100
if number >1000:
    total_bonus += number * 10/100
if number % 2 == 0:
    total_bonus += 1
elif number % 5 == 0:
    total_bonus += 2

print(total_bonus)
print(number + total_bonus)