chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50

count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

price_chicken_menu = count_chicken_menu * chicken_menu
price_fish_menu = count_fish_menu * fish_menu
price_vegetarian_menu = count_vegetarian_menu * vegetarian_menu

total_sum = price_vegetarian_menu + price_fish_menu + price_chicken_menu
price_desert = total_sum * 20 / 100

total_sum2 = total_sum + price_desert + delivery_price

print(total_sum2)