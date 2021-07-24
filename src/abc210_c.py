"""

"""

N, K = map(int, input().split())
candies = list(map(int, input().split()))

prev_color = candies[0]
streak = 1
streaks = []
for i in range(1, N):
    if candies[i] == prev_color:
        streak += 1
    else:
        streaks.append((prev_color, streak))
        streak = 1
        prev_color = candies[i]
else:
    streaks.append((prev_color, streak))
    prev_color = candies[i]

max_kinds = 0
for i, begin in enumerate(streaks[:-1]):
    got_colors = [begin[0]]
    num_candies = 1
    for next_streak in streaks[i+1:]:
        got_colors.append(next_streak[0])
        num_candies += next_streak[1]
        if not num_candies < K:
            break
    kinds = len(set(got_colors))
    max_kinds = max(max_kinds, kinds)
    if max_kinds == K:
        break

print(max_kinds)
