def solution(spell, dic):
    for chk in dic:
        all_spell = len(spell)
        for letter in spell:
            if chk.count(letter):
                all_spell -= 1
        if all_spell == 0:
            return 1
    return 2