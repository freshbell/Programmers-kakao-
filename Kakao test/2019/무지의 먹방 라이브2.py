def solution(food_times, k):
    food_times_list = []
    totalTime = 0

    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime+=food_times[i]

    if totalTime <= k:
        return -1

    food_times_list = sorted(food_times_list, key=lambda x:x[1])
    print(food_times_list)

    delTime = food_times_list[0][1]*len(food_times_list)
    i=1
    # print k
    # print delTime
    while delTime < k:
        k-=delTime
        delTime = (food_times_list[i][1]-food_times_list[i-1][1])*(len(food_times_list)-i)
        i+=1

    food_times_list = sorted(food_times_list[i-1:])
    print (food_times_list)
    # print food_times_list
    # print k
    return food_times_list[k%len(food_times_list)][0]+1

food_times = [3, 1, 2]
k = 5
solution(food_times,k)