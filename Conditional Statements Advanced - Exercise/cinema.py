screening_type = str(input())
rows = int(input())
columns = int(input())
income = 0

cinema_area = rows * columns

if screening_type == 'Premiere':
    income = cinema_area * 12
elif screening_type == 'Normal':
    income = cinema_area * 7.5
elif screening_type == 'Discount':
    income = cinema_area * 5

print(f'{income:.2f} leva.')