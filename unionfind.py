def find(id,i):
    if id[i] == i:
        return i
    else:
        temp = find(id,id[i])
        id[i] = temp
        return temp

def union(id,a,b):
    pa = find(id,a)
    pb = find(id,b)
    rank_a = id.count(pa)
    rank_b = id.count(pb)
    if pa != pb:
        if rank_a > rank_b:
            id[b] = pa
        else:
            id[a] = pb

if __name__=="__main__":
    n = int(input("Ingrese n: "))
    id = [i for i in range(n)]
    union(id,2,3)
    print(id)
    union(id,2,4)
    print(id)
    union(id,1,2)
    print(id)
    union(id,1,0)
    print(id)


