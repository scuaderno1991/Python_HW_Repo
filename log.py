import time
def timestamp(func):
    def wrapper():
        print(time.ctim())
        func()
        return wrapper

# @timestamp
# def hi():
#     print('hi')
# def main():
#     hi()
# main()