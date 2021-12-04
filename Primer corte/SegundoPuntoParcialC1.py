def sumaCuadrados(n) :
    #  Iterar i desde 1
    #  y n buscando
    #  el cuadrado de i
    #  y añadiendolo a la suma
    sum = 0
    for i in range(1, n + 1) :
        sum = sum + (i * i)
    return sum


n = 4
print(sumaCuadrados(n))

