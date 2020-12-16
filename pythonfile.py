def py_fun1(arg):
    res = py_fun4([1, 2, arg])
    return res


def py_fun2(a, b):
    c = a + b
    return c


def py_fun3(list):
    res = 0
    for item in list:
        res += item
    # look a comment
    return res


def py_fun4(list):
    res = [a + 1 for a in list if a < 3]
    return res
