age = int(input())
price_washing_maschine = float(input())
price_present = int(input())

saved_money = 0
money_for_birthday = 10
number_of_toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += (money_for_birthday - 1)
        money_for_birthday += 10
    else:
        number_of_toys += 1

saved_money += price_present * number_of_toys

diff = abs(saved_money - price_washing_maschine)
if saved_money >= price_washing_maschine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")