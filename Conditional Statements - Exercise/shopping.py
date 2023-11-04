budget = float(input())
number_video_cards = int(input())
number_cpu = int(input())
number_ram = int(input())

price_video_card = 250
total_sum_video_cards = price_video_card * number_video_cards
price_cpu = total_sum_video_cards * 35 / 100
price_ram = total_sum_video_cards * 10 / 100

total_sum_cpu = number_cpu * price_cpu
total_sum_ram = number_ram * price_ram

total_sum = total_sum_video_cards + total_sum_cpu + total_sum_ram

if number_video_cards > number_cpu:
    total_sum *= 85 / 100

left_money = abs(total_sum - budget)
if total_sum <= budget:
    print(f"You have {left_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_money:.2f} leva more!")