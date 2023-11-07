input_line = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_count_tickets = 0

while input_line != "Finish":
    movie = input_line
    capacity = int(input())
    command_line = input()
    current_movie_count = 0

    while command_line != "End":
        type_ticket = command_line
        current_movie_count += 1
        total_count_tickets += 1

        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1

        if current_movie_count == capacity:
            break
        command_line = input()

    percentage_tickets = current_movie_count / capacity * 100
    print(f"{movie} - {percentage_tickets:.2f}% full.")
    input_line = input()

print(f"Total tickets: {total_count_tickets}")
percent_students = student_tickets / total_count_tickets * 100
percent_standard = standard_tickets / total_count_tickets * 100
percent_kids = kids_tickets / total_count_tickets * 100
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")