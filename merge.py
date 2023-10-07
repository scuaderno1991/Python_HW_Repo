def merge_list(list1, list2):
    try:
        # Attempt to concatenate the lists
        sorted_list = list1 + list2
    except TypeError:
        # Handle the TypeError if list1 or list2 is not a list
        raise TypeError("Both inputs must be lists.")
    #if not isinstance(list1, int) or not isinstance(list2, int):
        #raise TypeError("Both inputs must be lists.")
    
    sorted_list = []
    sorted_list.extend(list1)
    sorted_list.extend(list2)
    
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
######################################################################################
list1 = [10,78,99,4,8,2]
list2 = [15,3,80,5,6]


print(merge_list(list1,list2))




