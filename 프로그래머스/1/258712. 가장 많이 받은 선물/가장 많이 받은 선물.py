from collections import Counter
def solution(friends, gifts):
    gifts_a = Counter(gift.split(' ')[0] for gift in gifts)
    gifts_b = Counter(gift.split(' ')[1] for gift in gifts)
    gifts_idx = {f:gifts_a[f] - gifts_b[f] for f in friends}
    
    cnt = Counter(gifts)
    get_gifts = dict.fromkeys(friends, 0)
    for k,v in cnt.items():
        a, b = k.split(' ')
        if v > cnt[f'{b} {a}']:
            get_gifts[a] += 1
        elif v == cnt[f'{b} {a}']:
            if gifts_idx[a] > gifts_idx[b]:
                get_gifts[a] += 1
    for i in range(len(friends)):
        for frnd in (set(friends)-set(friends[:i+1])):
            if all([(f'{friends[i]} {frnd}' not in gifts), (f'{frnd} {friends[i]}' not in gifts)]):
                if gifts_idx[friends[i]] > gifts_idx[frnd]:
                    get_gifts[friends[i]] += 1
                elif gifts_idx[friends[i]] < gifts_idx[frnd]:
                    get_gifts[frnd] += 1
                
    return max(get_gifts.values())