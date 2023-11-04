lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

capacity_aquarium = lenght_cm * width_cm * height_cm
capacity_litres = capacity_aquarium / 1000
occupied_space = percent / 100
litres_required = (capacity_litres * (1 - occupied_space))

print(litres_required)