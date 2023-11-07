count_tabs = int(input())
salary = int(input())
flag = False

for i in range(count_tabs):
    tab_name = input()
    if tab_name == 'Facebook':
        salary = salary - 150
    elif tab_name == 'Instagram':
        salary = salary - 100
    elif tab_name == 'Reddit':
        salary = salary - 50
    if salary <= 0:
        flag = True
        break

if flag:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")