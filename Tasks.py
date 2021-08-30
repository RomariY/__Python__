# string task
# st = 'Print only the words that start with s in this sentence'
# st = st.lower()
# words = st.split(' ')
# for word in words:
#     if word.startswith('s'):
#         print(word)
#     else:
#         continue

# Range
# list_nums = []
# for num in range(0, 101):
#     if num % 3 == 0:
#         list_nums.append('Fizz')
#     elif num % 5 == 0:
#         list_nums.append('Bazz')
#     elif num % 3 == 0 and num % 5 == 0:
#         list_nums.append('FizzBazz')
#     else:
#         list_nums.append(num)
# print(list_nums)


# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i%2==0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)

# print(myfunc('Anthropomorphism'))

# def has_33(nums):
#     for a in range(len(nums)-1):
#         if nums[a] == nums[a+1]:
#             return True
#         else:
#             continue

# print(has_33([1,2,3,3,4,5]))

# def spy_game(nums):
#     code = [0, 0, 7, 'x']
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)
#     return len(code) == 1

    
# print(spy_game([1,2,4,0, 0,0,7,5]))
# map function
# def sqrt(num):
#     return num**2

# my_nums = [1, 2, 3, 4, 5, 6, ]

# m = map(sqrt, my_nums)
# for k in m:
#     print(k)
# print(m)

# Filter Function
# my_nums = [1, 2, 3, 4, 5, 6, ]

# def check_even(num):
#     return num%2 == 0

# print(list(filter(check_even, my_nums)))
# print(list(filter(lambda num:num%2 == 0, my_nums)))