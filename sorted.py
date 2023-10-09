def sort_dictionary(input_dict):
    item = list(input_dict.items())
    n = len(item)
    
    for i in range (1,len(item)):
        current_dict = item[i]
        j = i-1
        
        while j>= 0 and current_dict[0] > item[j][0]:
            item[j+1] = item[j]
            j -= 1
            
        item[j+1] = current_dict
        
    sort_tuples = [(name,values[0]) for name, values in item]
    
    return sort_tuples

myDict = {'Tom': (5464512,24), 'Sara' : (5446987, 32), 'Mary': (1557896,20)}
sorted_dict = sort_dictionary(myDict)
print(sorted_dict)