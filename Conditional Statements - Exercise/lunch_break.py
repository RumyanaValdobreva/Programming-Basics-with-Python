import math

name_series = input()
duration_episode = int(input())
duration_break = int(input())

time_for_lunch = 1/8 * duration_break
time_to_relax = 1/4 * duration_break
time_left = duration_break - time_for_lunch - time_to_relax

if time_left >= duration_episode:
    print(f"You have enough time to watch {name_series} and left with {math.ceil(time_left - duration_episode)} minutes free time.")
elif time_left < duration_episode:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(duration_episode - time_left)} more minutes.")