def solution(players, callings):
    player_dic={key: i for i, key in enumerate(players)}
    
    for i in callings:
        idx=player_dic[i]
        player_dic[i]-=1
        player_dic[players[idx-1]]+=1
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players