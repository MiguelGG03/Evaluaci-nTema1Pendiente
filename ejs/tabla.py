def main4():
    print('El primer argumento hará referencia a las filas\n de una tabla, el segundo a las columnas.')
    print()
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


if __name__=='__main__':
    main4()