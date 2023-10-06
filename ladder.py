# def my_steps(n):
#     if n <= 1:
#         return n
#         return my_steps(n-1) + my_steps(n-2)


# print(my_steps(2))
 
#def countWays(s):
    #return my_steps(s + 1)


# def my_steps(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
    
#     # Create a list to store the number of ways to climb for each step.
#     steps = [0] * (n + 1)
    

#     steps[1] = 1
#     steps[2] = 2
    
   
#     for i in range(3, n + 1):
#         steps[i] = steps[i - 1] + steps[i - 2]
    
#     return steps[n]

def my_steps(n):
    if n<= 1 or n >= 25:
        raise ValueError("Integer is not correct")
    else:    
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

    # Initialize  to store the number of ways for the previous two steps.
    pre = 2
    pre1 = 1

    for i in range(3, n + 1):
        current = pre + pre1
        pre1 = pre
        pre = current

    return pre

#print(my_steps(2))
  
