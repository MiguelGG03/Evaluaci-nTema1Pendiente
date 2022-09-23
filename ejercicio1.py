def calculador(mdm,n):
    suma=0
    suma=mdm[n][0]+mdm[n][1]+mdm[n][2]
    if(suma!=mdm[n][3]):
        mdm[n][3]=suma
    else:
        return print('Fila {} correcta'.format(str(n+1)))



def main1():
    
    matriz=[ [1, 1, 1, 3],
            [2, 2, 2, 7],
            [3, 3, 3, 9],
            [4, 4, 4, 13]]
    qfdm=int(input('Que fila desea comprobar: '))
    qfdm=qfdm-1
    calculador(matriz,0)



if __name__=='__main__':
    main1()