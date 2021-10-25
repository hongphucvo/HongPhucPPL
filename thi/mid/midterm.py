from functools import reduce
f=lambda x: x*2
def iter(f,n):
    def exp(x):
        return reduce (lambda acc, ele: f(acc),range(1,n),f(x))
    return exp
print(iter(f,3)(3))



print(reduce(lambda acc,ele: acc**2, range(1,5),1**2))
