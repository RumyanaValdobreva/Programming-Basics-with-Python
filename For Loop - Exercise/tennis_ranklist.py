from math import floor

count_tournirs = int(input())
initial_points = int(input())

W = 2000
F = 1200
SF = 720

average_points = 0
count_win_tournirs = 0

for i in range(count_tournirs):
    position = input()

    if position == 'W':
        initial_points += W
        average_points += W
        count_win_tournirs += 1
    elif position == 'F':
        initial_points += F
        average_points += F
    elif position == 'SF':
        initial_points += SF
        average_points += SF

print(f'Final points: {initial_points}')
print(f'Average points: {floor(average_points / count_tournirs)}')
print(f'{count_win_tournirs / count_tournirs * 100:.2f}%')