month = input()
number_of_nights = int(input())

studio = 0
apartment = 0
total_sum_studio = 0
total_sum_apartment = 0

if month == 'May' or month == 'October':
  studio = 50
  apartment = 65
  if 7 < number_of_nights < 14:
      studio = studio - (studio * 0.05)
  elif number_of_nights > 14:
      studio = studio - (studio * 0.30)
      apartment = apartment - (apartment * 0.10)
elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
    if number_of_nights > 14:
        studio = studio - (studio * 0.20)
        apartment = apartment - (apartment * 0.10)
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if number_of_nights > 14:
        apartment = apartment - (apartment * 0.10)

total_sum_studio = number_of_nights * studio
total_sum_apartment = number_of_nights * apartment

print(f'Apartment: {total_sum_apartment:.2f} lv.')
print(f'Studio: {total_sum_studio:.2f} lv.')
