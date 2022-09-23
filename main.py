from ejs.ejercicio1 import *
from ejs.ejercicio2 import *
from ejs.ejercicio3 import *
from ejs.tabla import *


def main():
    seguir=True
    while(seguir==True):
        qedv=int(input('Que ejercicio desea ver (1) (2) (3) (4) : '))
        if(qedv==1):
            main1()
            desea=int(input('\nDesea seguir \n(0) No \n(1) Si\nRespuesta:'))
            if(desea==0):
                seguir=False
            else:
                seguir=True
        elif(qedv==2):
            main2()
            desea=int(input('\nDesea seguir \n(0) No \n(1) Si\nRespuesta:'))
            if(desea==0):
                seguir=False
            else:
                seguir=True
        elif(qedv==3):
            main3()
            desea=int(input('\nDesea seguir \n(0) No \n(1) Si\nRespuesta:'))
            if(desea==0):
                seguir=False
            else:
                seguir=True
        elif(qedv==4):
            main4()
            desea=int(input('\nDesea seguir \n(0) No \n(1) Si\nRespuesta:'))
            if(desea==0):
                seguir=False
            else:
                seguir=True




if __name__=='__main__':
    main()