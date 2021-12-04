#MERGE SORT

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
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

arr = [12, 11, 13, 5, 6, 7]
print("El array dado es:", end="\n")
printList(arr)
mergeSort(arr)
print("Sorted array es: ", end="\n")
printList(arr)

#INSERTION SORT

def insertionSort(arr):

    # Atravesar 1 para len (arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Mover elementos de arr [0..i-1], que son
        # mayor que la clave, a una posición por delante
        # de su posición actual
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


# Correr el codigo de prueba de abajo
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])