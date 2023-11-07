poor_grades = int(input())

input_line = input()
sum_grades = 0
count_grades = 0
last_problem = ''
count_poor_grades = 0

while input_line != 'Enough':
    last_problem = input_line
    current_grade = int(input())
    if current_grade <= 4:
        count_poor_grades += 1
    sum_grades += current_grade
    count_grades += 1

    if count_poor_grades >= poor_grades:
        break

    input_line = input()

if count_poor_grades == poor_grades:
    print(f'You need a break, {count_poor_grades} poor grades.')
else:
    print(f'Average score: {sum_grades / count_grades:.2f}')
    print(f'Number of problems: {count_grades}')
    print(f'Last problem: {last_problem}')