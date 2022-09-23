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

if __name__=='__main__':
    main2()