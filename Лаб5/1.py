def func1(n):
    def func2(x):
        return x+n
    return func2
func = func1(8)
print(func(2))
