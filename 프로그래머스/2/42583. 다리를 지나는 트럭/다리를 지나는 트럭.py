from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = 0
    time = 0
    queue = deque([0] * (bridge_length))
    
    while truck:
        bridge -= queue.popleft()
        
        if (bridge + truck[0]) <= weight:
            bridge += truck[0]
            queue.append(truck.popleft())
            time += 1
            
            if not truck:
                time += bridge_length
                break

        else:       
            queue.append(0)
            time += 1
            
    return time