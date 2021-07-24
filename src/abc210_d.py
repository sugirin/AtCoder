"""

"""
H, W, rail_cost = map(int, input().split())
station_costs = [list(map(int, input().split())) for _ in range(H)]

min_station_cost = min([c for row in station_costs for c in row])

station_points = []
for h in range(H):
    for w in range(W):
        if station_costs[h][w] == min_station_cost:
            station_points.append((h,w))

min_actual_cost = 10**10
for h,w in station_points:
    actual_costs = [[0 for __ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            actual_costs[i][j] = station_costs[i][j] + rail_cost*(abs(h-i)+abs(w-j)) + min_station_cost
    actual_costs[h][w] = 10**10
    min_actual_cost = min(min_actual_cost, *[c for row in actual_costs for c in row])

print(min_actual_cost)