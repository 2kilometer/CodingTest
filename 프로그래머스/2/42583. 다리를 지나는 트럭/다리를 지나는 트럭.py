from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    next_weights = truck_weights.popleft()
    
    queue = deque([0] * (bridge_length-1) + [next_weights])
    time = 1 if truck_weights else (1+bridge_length)
    
    while truck_weights:
        next_weights -= queue.popleft()
        
        if (next_weights+truck_weights[0]) <= weight:
            next_weights += truck_weights[0]
            
            queue.append(truck_weights.popleft())
            time += 1
            
            if not truck_weights:
                time += bridge_length
                break

        else:       
            queue.append(0)
            time += 1
            
    return time