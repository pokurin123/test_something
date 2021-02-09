x = [1,2,3]

def add(a,b):
    for i in range(len(a)):
        x[i] += b

add(x,1)
print(x)