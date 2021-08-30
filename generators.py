import datetime
def create_cube(n):
    result = []
    for x in range(n+1):
        result.append(x**3)
    return result


start_1 = datetime.datetime.now().microsecond
print(create_cube(10))
end_1 = datetime.datetime.now().microsecond
# unload the memory
print(end_1-start_1)
def create_cube(n):
    for x in range(n+1):
        yield x**3

start_1 = datetime.datetime.now().microsecond
print(list(create_cube(10)))
end_1 = datetime.datetime.now().microsecond
print(end_1-start_1)

# iter
text = "hello"
text_iter = iter(text)

print(next(text_iter))
print(next(text_iter))
print(next(text_iter))
print(next(text_iter))
print(next(text_iter))


