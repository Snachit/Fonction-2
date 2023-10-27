def max(T):
    for i in range(len(T)):
        Max=T[0]
        if (Max<T[i]):
            Max=T[i]
        return Max
def min(T):
    for i in range(len(T)):
        Min=T[0]
        if (Min>T[i]):
            Min=T[i]
        return Min
def reverse(T):
    V=[]
    for i in range(len(T)-1,-1,-1):
        V.append(T[i])
    return V
T=[]
for i in range(10):
    x=int(input(f"entre le nombre {i+1}:"))
    T.append(x)
print("Le minimum de tableau est",min(T))
print("Le maximum de tableau est",max(T))
print (reverse(T))