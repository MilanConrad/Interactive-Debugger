

def py_fun1(arg):
    arg += 1
    res = py_fun2(1, arg)
    res += 1
    return res


def py_fun2(a, b):
    c = a + py_fun5(b)
    return c


def py_fun5(arg):
    res = arg * 10
    res *= 2
    return res


def py_fun3(list):
    res = 0
    for item in list:
        res += item
    # look a comment
    return res


def py_fun4(list):
    res = [a + 1 for a in list if a < 3]
    return res


print(py_fun1(1))