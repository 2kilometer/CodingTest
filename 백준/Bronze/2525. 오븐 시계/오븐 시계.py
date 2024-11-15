h, m = map(int, input().split())
cook = int(input())

max_time = (23 * 60 + 59)
needed_time = (h * 60 + m) + cook

if needed_time > max_time:
    needed_time = needed_time - (max_time + 1)

print(needed_time // 60, needed_time % 60)