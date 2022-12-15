def f1(x):
    return 1 + x
def f2(x, f):
    return f(x) * 3
print(f2(3, f1))
