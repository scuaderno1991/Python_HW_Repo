def allcaps(func):
    def wrapper():
       
        res = func()
        if isinstance(res,str):
            return res.capitalize()
        else:
            return res

    return wrapper
   
  
# @allcaps
# def greet():
#     return "hello World!"

# def main():
#     greet()
# main()

# print(greet())