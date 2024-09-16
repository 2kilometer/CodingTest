x = input()
y = input()
quadrant = [(0, 0), (1, 0), (1, 1), (0, 1)]

print(quadrant.index((('-' in x), ('-' in y))) + 1)