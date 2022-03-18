# Arguments :
# args - Undefined number of lists
# sep - random char
# return value : list
# This functions joins lists and between them appends the given char 'sep'
def join(*args, sep='-'):
    if not args:
        return None

    list1 = []
    [(list1.extend(x), list1.append(sep)) for x in args]

    list1.pop()
    return list1
