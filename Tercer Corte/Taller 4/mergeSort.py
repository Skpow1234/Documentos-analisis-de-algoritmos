import time
import numpy as np

start_time = time.time()*1000
# MERGE SORT
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = []
for x in range(500):
    arr.append(np.random.randint(1,50))

print("Given array is", end="\n")
printList(arr)
mergesort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
end_time=time.time()*1000

print("--- %s seconds ---" % (end_time - start_time))