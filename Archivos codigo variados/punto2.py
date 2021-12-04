"""El arreglo debe estar ordenado para el funcionamiento del algoritmo"""
def sumMaxima(arr,m): 
    n = 0
    i = 0
    a = 0
    sumaSubArreglo=0
    if len(arr)%2==0:   
        n = 0
    else: 
        n = 1
    lista = []
    while n < len(arr):
        lista.clear()
    for x in range(len(arr)//2):
        sumaSubArreglo+=arr[n]
        lista.append(arr[n])
        n+=1
    if sumaSubArreglo > a:
        a = sumaSubArreglo
    sumaSubArreglo=0
    if(m > len(arr)//2):  
        if(m%2==0):
            if(len(arr)%2!=0):
                n=(len(arr)//2)
        else:
            n=(len(arr)//2)-1
        i = (len(arr))-m
    else:
        if(len(arr)%2!=0):
            n=(len(arr)//2)
        else:
            n=(len(arr)//2)-1
        i = (len(arr))-m
    while n>=i:
        a+=arr[n]
        n-=1   
    return a

print(sumMaxima([1,7,8,9,13,16,21],6))
