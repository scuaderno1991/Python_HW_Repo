

######################################################################################################
def cacti_number(func):
    def wrapper(my_arr):
        row = len(my_arr) # num of rows in matr
        col = len(my_arr[0]) #num of columns
        total = 0 
        for j in range(row):
            for k in range(col):
                if my_arr[j][k] == 0:
                    #  ele at the toprow or above is 0.
                    #  ele at the bottom row or below  0.
                    #  ele at the rightmost column or right is 0.
                    #  ele at the top row or leftmost column or if the element at the top-left is zero.
                    #  ele at the top row or rightmost column or if the element at the top-right is zero
                    #  ele at the bottom row or leftmost column or if the element at the bottom-left is zero. 
                     # ele at the bottom row or rightmost column or if the element at the bottom-right is zero   
                    if (j == 0 or my_arr[j-1][k] == 0) and (j == row-1 or my_arr[j+1][k] == 0) and \
                       (k == 0 or my_arr[j][k-1] == 0) and (k == col-1 or my_arr[j][k+1] == 0) and \
                       (j == 0 or k == 0 or my_arr[j-1][k-1] == 0) and (j == 0 or k == col-1 or my_arr[j-1][k+1] == 0) and \
                       (j == row-1 or k == 0 or my_arr[j+1][k-1] == 0) and(j == row-1 or k == col-1 or my_arr[j+1][k+1] == 0):
                        my_arr[j][k] = 1 #if conditions are true set current element pos to 1
                        total += 1 #sum number of 1s 
        return total
    return wrapper

def main():
    array = [
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0]
    ]

    
    cacti_count = cacti_number(array)

    # Display the result.
    print(f"Number of cacti is {cacti_count}")
main()
