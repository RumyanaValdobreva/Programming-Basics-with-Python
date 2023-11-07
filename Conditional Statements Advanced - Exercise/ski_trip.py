days_to_stay = int(input())
type_room = input()
review = input()

overnight_stays = days_to_stay - 1
price_night = 0

price_room_one_person = 18
price_apartment = 25
price_president_apartment = 35

if type_room == 'room for one person':
    price_night = price_room_one_person
    if 0 < days_to_stay <= 10:
        price_night = price_room_one_person
    elif 10 <= days_to_stay <=15:
        price_night = price_room_one_person
    elif days_to_stay > 15:
        price_night = price_room_one_person
elif type_room == 'apartment':
    price_night = price_apartment
    if 0 < days_to_stay < 10:
        price_night = price_apartment * 0.70
    elif 10 <= days_to_stay <= 15:
        price_night = price_apartment * 0.65
    elif days_to_stay > 15:
        price_night = price_apartment / 2
elif type_room == 'president apartment':
    price_night = price_president_apartment
    if 0 < days_to_stay < 10:
        price_night = price_president_apartment * 0.90
    elif 10 <= days_to_stay <= 15:
        price_night = price_president_apartment * 0.85
    elif days_to_stay > 15:
        price_night = price_president_apartment * 0.80

total_price = overnight_stays * price_night

if review == 'positive':
    total_price = total_price * 1.25
    print(f'{total_price:.2f}')
elif review == 'negative':
    total_price = total_price * 0.90
    print(f'{total_price:.2f}')