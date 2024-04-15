def solution(score):
    mean = [(x[0]+x[1])/2 for x in score]
    mean_sort = sorted(mean.copy(), reverse=True)

    return [mean_sort.index(v)+1 for v in mean]