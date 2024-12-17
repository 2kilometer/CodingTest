def solution(video_len, pos, op_start, op_end, commands):
    video_time = int(video_len[:2]) * 60 + int(video_len[-2:])
    pos_time = int(pos[:2]) * 60 + int(pos[-2:])
    op_start_time = int(op_start[:2]) * 60 + int(op_start[-2:])
    op_end_time = int(op_end[:2]) * 60 + int(op_end[-2:])
    
    def check_time(time):
        if time > video_time:
            return video_time
        
        if time <= 0:
            time = 0
        if op_start_time <= time <= op_end_time:
            time = op_end_time
        return time
    
    pos_time = check_time(pos_time)
    for cmd in commands:    
        if cmd == "prev":
            pos_time = check_time(pos_time - 10)
        elif cmd == "next":
            pos_time = check_time(pos_time + 10)
    
    return f"{(pos_time // 60):02}:{(pos_time % 60):02}"