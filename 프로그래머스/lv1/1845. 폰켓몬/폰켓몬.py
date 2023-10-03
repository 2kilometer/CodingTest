def solution(nums):
    pokemon = []
    for i in range(len(nums)):
        if pokemon : 
            if nums[i] not in pokemon:
                pokemon.append(nums[i])
        else : pokemon.append(nums[i])
    
    nums_cnt = len(nums)/2
    pokemon_cnt = len(pokemon)
    if pokemon_cnt > nums_cnt:
        answer = nums_cnt
    else : 
        answer = pokemon_cnt
    return answer