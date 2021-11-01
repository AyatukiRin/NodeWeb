from math import sqrt

area, num_detector, radius = map(int, input().split())
detector_list = []
count = 0
for i in range(num_detector):
    detector_list.append(tuple(map(int, input().split())))
for position_x in range(1, area + 1):
    for position_y in range(1, area + 1):
        for detector_position in detector_list:
            distance = sqrt(pow(detector_position[0] - position_x, 2) + pow(detector_position[1] - position_y, 2))
            if distance <= radius:
                count += 1
                break
print(count)