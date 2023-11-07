needed_money = float(input())
available_money = float(input())

days_count = 0
spend_count = 0

while available_money < needed_money:
    if spend_count == 5:
        break
    action = input()
    amount = float(input())

    days_count += 1

    if action == 'spend':
        spend_count += 1
        available_money -= amount
        if available_money < 0:
            available_money = 0
    elif action == 'save':
        spend_count = 0
        available_money += amount

if spend_count == 5:
    print("You can't save the money.")
    print(days_count)
else:
    print(f'You saved the money for {days_count} days.')