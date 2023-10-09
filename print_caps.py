def allcaps(func):
    def wrapper(*args,**kwargs):
       
        res = func(*args, **kwargs)
        if isinstance(res,list):
            uppercase_list = [s.upper() for s in res]
            return uppercase_list
        else:
            return res

    return wrapper

# @allcaps
# def get_string():
#     return ["apple", "oranges", "banana"]
# result = get_string()

# print(result)

# def allcaps(func):
#     def wrapper(*args,**kwargs):
       
#         res = func(*args, **kwargs)
#         if isinstance(res,str):
#             return res.capitalize()
#         else:
#             return res

#     return wrapper 
  
# @allcaps
# def greet():
#     return "hello World!"

# def main():
#     greet()
# main()

# print(greet())