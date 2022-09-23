from ejs.ejercicio1 import *
from ejs.ejercicio2 import *
from ejs.ejercicio3 import *
from ejs.tabla import *


def main():
    qedv=int(input('Que ejercicio desea ver (1) (2) (3) (4) : '))
    if(qedv==1):
        main1()
    if(qedv==2):
        main2()
    if(qedv==3):
        main3()
    if(qedv==4):
        main4()




if __name__=='__main__':
    main()