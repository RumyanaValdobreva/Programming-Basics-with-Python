book_name = input()

count_books = 0
current_book = input()
is_book_found = False

while current_book != 'No More Books':
    if book_name == current_book:
        is_book_found = True
        break

    count_books += 1
    current_book = input()

if is_book_found:
    print(f'You checked {count_books} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {count_books} books.')