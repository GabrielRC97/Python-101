import functools

numbers = [1,2,3,4]

def accum(counter, item):
    print('counter => ',counter)
    print('item => ',item)
    return counter + item

result = functools.reduce(accum, numbers)

print (result)

result_v2 = functools.reduce(lambda x, y: max(x, y), numbers)

print (result_v2)