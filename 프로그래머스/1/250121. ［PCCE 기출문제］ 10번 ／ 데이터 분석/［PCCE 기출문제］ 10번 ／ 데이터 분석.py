import pandas as pd
def solution(data, ext, val_ext, sort_by):
    col = {"code":0, "date":1, "maximum":2, "remain":3}
    data = pd.DataFrame(data)
    data = data[data[col[ext]] < val_ext].sort_values(col[sort_by])
    return data.values.tolist()