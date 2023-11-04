count_pen = int(input())
count_markers = int(input())
detergent_litres = int(input())
discount = int(input())

price_pen = 5.80
price_markers = 7.20
detergent_price = 1.20

total_price_pen = count_pen * price_pen
total_price_markers = count_markers * price_markers
total_price_detergent = detergent_litres * detergent_price

total_price_without_discount = total_price_pen + total_price_markers + total_price_detergent
total_price_with_discount = total_price_without_discount - (total_price_without_discount * discount / 100)

print(total_price_with_discount)