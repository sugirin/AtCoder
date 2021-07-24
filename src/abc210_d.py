"""
https://atcoder.jp/contests/abc210/tasks/abc210_d
"""
H, W, rail_cost = map(int, input().split())
station_costs = [list(map(int, input().split())) for _ in range(H)]

dp = [[0 for w in range(W)] for h in range(H)]
for h in range(H):
    for w in range(W):
        if h==0 and w==0:
            dp[h][w] = station_costs[h][w]
        elif h==0:
            dp[h][w] = min(dp[h][w-1] + rail_cost, station_costs[h][w])
        elif w==0:
            dp[h][w] = min(dp[h-1][w] + rail_cost, station_costs[h][w])
        else:
            from_up = dp[h-1][w] + rail_cost
            from_left = dp[h][w-1] + rail_cost
            dp[h][w] = min(from_up, from_left, station_costs[h][w])

X = [[0 for w in range(W)] for h in range(H)]
for h in range(H):
    for w in range(W):
        if h==0 and w==0:
            X[h][w] = 10**10
        elif h==0:
            X[h][w] = dp[h][w-1] + rail_cost + station_costs[h][w]
        elif w==0:
            X[h][w] = dp[h-1][w] + rail_cost + station_costs[h][w]
        else:
            X[h][w] = min(dp[h-1][w], dp[h][w-1]) + rail_cost + station_costs[h][w]

ans = min([x for _ in X for x in _])

dp = [[0 for w in range(W)] for h in range(H)]
for h in range(H):
    for w in reversed(range(W)):
        if h==0 and w==W-1:
            dp[h][w] = station_costs[h][w]
        elif h==0:
            dp[h][w] = min(dp[h][w+1] + rail_cost, station_costs[h][w])
        elif w==W-1:
            dp[h][w] = min(dp[h-1][w] + rail_cost, station_costs[h][w])
        else:
            from_up = dp[h-1][w] + rail_cost
            from_right = dp[h][w+1] + rail_cost
            dp[h][w] = min(from_up, from_right, station_costs[h][w])

X = [[0 for w in range(W)] for h in range(H)]
for h in range(H):
    for w in reversed(range(W)):
        if h==0 and w==W-1:
            X[h][w] = 10**10
        elif h==0:
            X[h][w] = dp[h][w+1] + rail_cost + station_costs[h][w]
        elif w==W-1:
            X[h][w] = dp[h-1][w] + rail_cost + station_costs[h][w]
        else:
            X[h][w] = min(dp[h-1][w], dp[h][w+1]) + rail_cost + station_costs[h][w]

ans = min(ans, min([x for _ in X for x in _]))

print(ans)