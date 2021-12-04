import time
import numpy as np

start_time = time.time()*1000

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = []
for x in range(500):
    arr.append(np.random.randint(1,50))

print("ANTES")
printList(arr)
insertionSort(arr)
print("DESPUES")
printList(arr)

end_time=time.time()*1000

print("--- %s seconds ---" % (end_time - start_time))