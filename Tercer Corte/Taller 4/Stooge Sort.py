# Programa en Python para implementar el ordenamiento de Stooge

def stoogesort(arr, l, h):
	if l >= h:
		return

	
    # El primer elemento es menor que el ultimo, cambialos
	if arr[l]>arr[h]:
		t = arr[l]
		arr[l] = arr[h]
		arr[h] = t

	# Si hay más de 2 elementos en
    # la matriz
	if h-l + 1 > 2:
		t = (int)((h-l + 1)/3)

		# Ordene de forma recursiva los primeros 2/3 elementos
		stoogesort(arr, l, (h-t))

		# Ordena recursivamente los últimos 2/3 elementos
		stoogesort(arr, l + t, (h))

		# Ordene de forma recursiva los primeros 2/3 elementos
# nuevamente para confirmar
		stoogesort(arr, l, (h-t))


# derivador de la función de ordenamiento
arr = [2, 4, 5, 3, 1, 10, 5, 9, 8, 15, 1, 20, 1050, 105, 522, 139, 589, 965, 845, 1552, 19657, 3241354, 654654, 1324874, 7261, 3748646, 321387, 87968, 53487, 377431, 387315]
n = len(arr)

stoogesort(arr, 0, n-1)

for i in range(0, n):
	print(arr[i], end = ' ')


