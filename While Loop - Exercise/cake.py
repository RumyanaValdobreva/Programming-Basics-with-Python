width = int(input())
lenght = int(input())

no_more_pieces = False

count_pieces_cake = width * lenght

input_line = input()
while input_line != 'STOP':
    current_pieces_cake = int(input_line)
    count_pieces_cake -= current_pieces_cake

    if count_pieces_cake <= 0:
        no_more_pieces = True
        break

    input_line = input()

if no_more_pieces:
    print(f'No more cake left! You need {abs(count_pieces_cake)} pieces more.')
else:
    print(f'{count_pieces_cake} pieces are left.')