stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
l = min([stations[i]-stations[i-1] for i in range(1, len(stations[1:]))]) + 0.0
r = max([stations[i]-stations[i-1] for i in range(1, len(stations[1:]))]) + 0.0

while l < r:
