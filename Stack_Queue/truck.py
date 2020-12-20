import time

def solution(bridge_length, weight, truck_weights):
    answer = 0
    return answer


'''예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다.
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 '''

time = 0

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

currentWeight = []
lengthStatus = []

def onTruck(truckIndex) : 
    global time
    currentWeight.append(truck_weights[truckIndex])
    
    if (sum(currentWeight) > weight) : 
        print("허용 무게 초과")
        currentWeight.pop()
        time += 1
    else : 
        lengthStatus.append(1)
        print("현재 다리에 올라온 트럭")
        print(currentWeight)
        time += 1
    