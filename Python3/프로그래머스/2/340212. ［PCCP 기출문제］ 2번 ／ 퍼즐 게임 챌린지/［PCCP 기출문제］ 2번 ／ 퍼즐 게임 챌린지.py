import math 
def solution(diffs, times, limit):
    def check(level):
        used_time = times[0]
        for i in range(1, len(diffs)):
            if diffs[i] > level:
                used_time += times[i] + ((diffs[i] - level) * (times[i-1] + times[i]))
            else:
                used_time += times[i]
        return used_time
    
    def div(level_max, level_min):
        if (level_max - level_min) <= 1:
            if check(level_min) > limit:
                return level_max
            return level_min
        
        chk_level = level_max - math.floor((level_max - level_min) / 2)
        
        if check(chk_level) > limit:
            level_min = chk_level
        else:
            level_max = chk_level
            
        return div(level_max, level_min)    

    return div(max(diffs), 1)