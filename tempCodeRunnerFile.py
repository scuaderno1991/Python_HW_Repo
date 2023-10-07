    temp = 0
    for i in range(0,len(sorted_list)):
        min = i 
        for j in range(0,len(sorted_list)):
            if sorted_list[min] < sorted_list[j]:
                temp = sorted_list[min]
                sorted_list[min] = sorted_list[j]
                sorted_list[j] = temp
    return sorted_list  