import math

record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

total_distance_seconds = distance_meters * time_seconds
additional_seconds = math.floor(distance_meters / 15) * 12.5

total_seconds = total_distance_seconds + additional_seconds

if total_seconds < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_seconds - record_seconds:.2f} seconds slower.")