price_training = int(input())
price_shoes = price_training - (price_training * 40/100)
price_uniform = price_shoes - (price_shoes * 20/100)
price_ball = price_uniform / 1/4
price_accessories = price_ball / 1/5

total_sum = price_training + price_shoes + price_uniform + price_ball + price_accessories

print(total_sum)