from collections import Counter
dices = input().split()
dices_count = Counter(dices)

if len(dices_count) == 1:
    print(10000 + int(dices[0]) * 1000)

elif len(dices_count) == 2:
    print(1000 + int(dices_count.most_common(1)[0][0]) * 100)

else:
    print(max(map(int, dices)) * 100)