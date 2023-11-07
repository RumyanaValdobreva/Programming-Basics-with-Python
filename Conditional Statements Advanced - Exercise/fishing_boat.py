budget = int(input())
season = input()
count_fisherman = int(input())

price = 0

if season == 'Winter':
    price = 2600
    if count_fisherman <= 6:
        price *= 0.90
    elif 7 <= count_fisherman <= 11:
        price *= 0.85
    elif count_fisherman >= 12:
        price *= 0.75
elif season == 'Spring':
    price = 3000
    if count_fisherman <= 6:
        price *= 0.90
    elif 7 <= count_fisherman <= 11:
        price *= 0.85
    elif count_fisherman >= 12:
        price *= 0.75
elif season == 'Summer' or 'Autumn':
    price = 4200
    if count_fisherman <= 6:
        price *= 0.90
    elif 7 <= count_fisherman <= 11:
        price *= 0.85
    elif count_fisherman >= 12:
        price *= 0.75

if count_fisherman % 2 == 0:
    if season != 'Autumn':
        price *= 0.95

diff = abs(price - budget)
if price > budget:
    print(f'Not enough money! You need {diff:.2f} leva.')