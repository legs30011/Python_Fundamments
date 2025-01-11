"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""
def custom_max (n1:int,n2:int):
    if n1 > n2:
        return n1
    else:
        return n2
print (custom_max(1,2))


"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""
def max_3_num(a:int,b:int,c:int):
    if a >b and a>c :
        return a
    elif b>a and b>c:
        return 
    else:
        return c
print(max_3_num(345345,34534,435))

"""
4- Escribir una función que tome un carácter y devuelva 
True si es una vocal, de lo contrario devuelve False.

"""
def vocal(letra):
    vocal=['a','e','i','o','u']
    if letra in vocal:
        return True
    else:
        return False
print(vocal('a'))
"""
5- Escribir una función sum() y una función multip() 
que sumen y multipliquen respectivamente todos los números 
de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y 
multip([1,2,3,4]) debería devolver 24.
"""
def sum(list):
    result = 0
    for n in list:
        result = result + n
    print (result)
print(sum([1,2,3,4]))

def mult(list):
    resultado = 1
    for n in list:
        resultado = resultado *n
    print (resultado)

print(mult([1,2,3,4]))
    


"""
6- Definir una función inversa() que calcule la inversión 
de una cadena. Por ejemplo la cadena "estoy probando" debería devolver 
la cadena "odnaborp yotse"
"""
"""
def inversion(cadena):
    tamaño= -(len(cadena)-1)
    nueva_cadena= str()
    for n in range(tamaño,1):
        n=abs(n)
        nueva_cadena += cadena[n]
    print(nueva_cadena)
inversion('hola')"""

def inversa(cadena):
    cadena= cadena[::-1]
    print(cadena)
inversa('hola')


"""
7 - Definir una función es_palindromo() que reconoce 
palíndromos (es decir, palabras que tienen el mismo aspecto 
escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def palindromo(cadena):
    if cadena[::-1] == cadena:
        return True
    else:
        return False
print(palindromo('radar'))


"""
8- Definir una función superposicion() que tome 
dos listas y devuelva True si tienen al menos 1 miembro en 
común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""
def superposicion(lista1,lista2):
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True
    return False
print(superposicion([1,2,3],[3,7,8]))


"""
9- Definir una función generar_n_caracteres() que tome un 
entero n y devuelva el caracter multiplicado 
por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres(caracter,n):
    string = caracter
    print(caracter * n)
    """for i in range(1,n):
        string += caracter
    print(string)
    """

generar_n_caracteres('s',2)

"""
10- Definir un histograma procedimiento() que tome una lista de números 
enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) 
debería imprimir lo siguiente:

****
********* 
*******
"""
def procedimiento(lista):
    for n in lista:
        caracter = 'x' * n
        print(f'{caracter}\n')
procedimiento([5,3,2])