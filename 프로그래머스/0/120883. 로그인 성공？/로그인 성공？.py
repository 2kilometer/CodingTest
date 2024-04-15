import numpy as np
def solution(id_pw, db):
    _id, _pw = id_pw
    db = np.array(db)
    chk_id = db[np.where(db[:,0] == _id)].tolist()
    
    if chk_id:
        if chk_id[0][1] == _pw:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"