name_actor = input()
points_academy = float(input())
n = int(input())

has_required_scores = False
threshold_of_points = 1250.5

for i in range(n):
    name = input()
    points = float(input())
    points_academy = points_academy +((len(name) * points) / 2)

    if points_academy > threshold_of_points:
        has_required_scores = True
        break
    else:
        has_required_scores = False

if has_required_scores:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_academy:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {threshold_of_points - points_academy:.1f} more!")