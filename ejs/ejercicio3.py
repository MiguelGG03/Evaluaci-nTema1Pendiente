def numeros_del_a_al_b(a,b,salto):
    lista_devuelta=[]
    for i in range(a,b+1,salto):
        lista_devuelta.append(i)
    return lista_devuelta

def main3():
    print('Secuencias disponibles:\n\n'
            '(1) Todos los números del 0 al 10 [0, 1, 2, ..., 10]\n'
            '(2) Todos los números del -10 al 0 [-10, -9, -8, ..., 0]\n'
            '(3) Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]\n'
            '(4) Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]\n'
            '(5) Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]')
    select=int(input('\nSeleccione una de las 5 opciones (introduzca un número del 1 al 5):\n'))
    if(select==1):
        print('Aquí tienes una lista con la secuencia\n{}'.format(numeros_del_a_al_b(0,10,1)))
    elif(select==2):
        print('Aquí tienes una lista con la secuencia\n{}'.format(numeros_del_a_al_b(-10,0,1)))
    elif(select==3):
        print('Aquí tienes una lista con la secuencia\n{}'.format(numeros_del_a_al_b(0,20,2)))
    elif(select==4):
        print('Aquí tienes una lista con la secuencia\n{}'.format(numeros_del_a_al_b(-20,0,2)))
    elif(select==5):
        print('Aquí tienes una lista con la secuencia\n{}'.format(numeros_del_a_al_b(0,50,5)))
    else:
        raise Exception('Eso no es un número del 1 al 5.')





if __name__=='__main__':
    main3()