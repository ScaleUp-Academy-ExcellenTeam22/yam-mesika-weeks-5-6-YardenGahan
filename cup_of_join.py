"""
 This functions joins lists and between them appends the given char 'sep'

 @param args - Undefined number of lists
 @param sep - random char
 @return - list
"""


def join(*args, sep='-'):
    [x.append(sep) for x in args]

    joined_list = [val for sublist in args for val in sublist]
    joined_list.pop()

    return joined_list
