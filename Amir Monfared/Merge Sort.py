def mergesort2(low,high):
    mid = 0
    if low < high :
        mid = (low + high) // 2
        mergesort2(low,mid)
        mergesort2(mid+1 , high)
        merge2(low, mid, high)


def merge2(low,mid,high):
    i,j,k = 0
    U = list(range(low,high))
    i,j, 