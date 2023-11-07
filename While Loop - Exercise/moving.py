widht_free_space = int(input())
lenght_free_space = int(input())
height_free_space = int(input())

volume = widht_free_space * lenght_free_space * height_free_space
sum_boxes = 0
input_line = input()

while input_line != 'Done':
    boxes = int(input_line)
    sum_boxes += boxes

    if sum_boxes >= volume:
        break

    input_line = input()

diff = abs(sum_boxes - volume)
if sum_boxes >= volume:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')