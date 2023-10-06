def merge_list(list1, list2):
    sorted_list = []
    sorted_list.extend(list1)
    sorted_list.extend(list2)
    
    # if not isinstance(merge_list, int):
    #     raise ValueError("input must be an integer")
    
    temp = 0
    for i in range(0,len(sorted_list)):
        min = i 
        for j in range(0,len(sorted_list)):
            if sorted_list[min] < sorted_list[j]:
                temp = sorted_list[min]
                sorted_list[min] = sorted_list[j]
                sorted_list[j] = temp
    return sorted_list   
    #print(f"Original List1: {list1} \nOriginal List2: {list2}")
    
    #sorted_list.sort(reverse = False)
    #print(f"Sorted List: {sorted_list}")
    
#list1 = [10,78,99,4,8,2]
#list2 = [15,3,80,5,6]

#merge_list(list1,list2)