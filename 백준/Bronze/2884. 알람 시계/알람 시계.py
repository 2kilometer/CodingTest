h, m = map(int, input().split())

wakeup_time = ((h * 60) + m) - 45

if wakeup_time >= 0:
    print(wakeup_time//60, wakeup_time%60)
else:
    print(23, 60 + wakeup_time)