# Evaluaci-nTema1Pendiente

El enlace a la tarea**Evaluación Tema 1 Pendiente** es el siguiente: [GitHub](https://github.com/migueliiin/Evaluaci-nTema1Pendiente.git)

## Ejercicio 1

El código del ejercicio es el siguiente:

```
    def calculador(mdm,n):
    suma=0
    suma=mdm[n][0]+mdm[n][1]+mdm[n][2]
    if(suma!=mdm[n][3]):
        antiguo=mdm[n][3]
        mdm[n][3]=suma
        return print('Hemos cambiado el {} por
         un {} en la Fila {}. [{}, {}, {}, {}]'.format(str(antiguo),str(suma),str(n+1),mdm[n][0],mdm[n][1],mdm[n][2],mdm[n][3]))
    else:
        return print('Fila {} correcta. [{}, {}, {}, {}]'.format(str(n+1),mdm[n][0],mdm[n][1],mdm[n][2],mdm[n][3]))



def main1():
    
    matriz=[ [1, 1, 1, 3],
            [2, 2, 2, 7],
            [3, 3, 3, 9],
            [4, 4, 4, 13]]
    print('-----MATRIZ-----')
    print(matriz)
    print('--------------')
    qfdm=int(input('Que fila desea comprobar: '))
    qfdm=qfdm-1
    calculador(matriz,qfdm)
```

## Ejercicio 2

El código del ejercicio es el siguiente:

```
        
    def lectordelistas(lista):
    cont=0
    listaseparada=[]

    while(cont<len(lista)):
        if(lista[cont]!=' '):
            listaseparada.append(lista[cont])
            cont=cont+1
        else:
            cont=cont+1

    if(3<=len(listaseparada)<10):
        return True
    else:
        return False

def main2():
    p=input('Introduzca una cadena de texto mayor o igual que 3 y a su vez menor que 10 (los espacios no se cuentan como caracter): \n')
    print(lectordelistas(p))
```

## Ejercicio 4

El código del ejercicio es el siguiente:

```
        
    a=int(input('Introduzca un numero entre el 1 y el 9: '))
    b=int(input('Introduzca otro numero entre el 1 y el 9: '))
    if(1<=a<=9 and 1<=b<=9):
        pass
    elif(a=='' or b==''):
        raise Exception('Debe introducir ambas veces un numero')
    else:
        raise Exception('Los numeros deben estar comprendidos entre el 1 y el 9')
    for i in range(a):
        print()
        for j in range(b):
            print(" * ", end='')
```