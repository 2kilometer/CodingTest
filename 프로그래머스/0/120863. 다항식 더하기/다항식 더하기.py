def solution(polynomial):
    _x = 0
    _constant = 0

    for v in polynomial.split(' + '):
        if v.isdigit():
            _constant += int(v)
        else:
            _x += 1 if v == 'x' else int(v[:-1])

    if _x == 0:
        return str(_constant)
    elif _constant == 0:
        return f'{_x}x' if _x != 1 else 'x'
    else:
        return f'{_x}x + {_constant}' if _x != 1 else f'x + {_constant}'