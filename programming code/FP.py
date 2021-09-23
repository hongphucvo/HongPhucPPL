def lessThan(lst,n):
    result=[x for x in lst if x<n]
    return result

def lstSquare(n):
    k=list(range(1,n+1))
    return list(map(lambda x:x**2,k))

def lstSquare2(n):
    if(n==0): return []
    return lstSquare2(n-1) + [n**2]

def flatten(lst):
    if(len(lst)==0):return[]
    else: return flat(lst,len(lst)-1)

def flat(lst,n):
    if(n==0):return lst[0]
    else: return flat(lst,n-1)+lst[n]
    
flatten([[1,2],[1,2,3,4]])

def dist(lst,n):
    return [(x,n) for x in lst]

def dist(lst,n):
    if(len(lst)==0): return[]
    return pair(lst,n,len(lst)-1)
def pair(lst,n,last):
    if(last==0): return [(lst[0],n)]
    return pair(lst,n,last-1)+[(lst[last],n)]


def lessThan(lst,n):
    return list(filter(lambda x:lt(x,n),lst))
def lt(x,n):
    return(x<n)

def dist(lst,n):
    return list(map(lambda x:pair(x,n),lst))
def pair(x,n):
    return (x,n)

def flatten2(lst):
    return list(map(lambda x: flat(x),lst))
def flat2(lst):
    return lst

def powGen(x):
    def f(y):
        return y**x
    return f
