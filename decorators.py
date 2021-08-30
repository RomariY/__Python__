def new_decorator(original_func):
    def wrap_func():
        print("Some text before func")
        original_func()
        print("Some code after func")
    return wrap_func

@new_decorator
def hello():
    print("Hello World!")

print(hello()) 

