

import math

def hash(palabra):
    nosirve=[0,7,8,9,10,13,27,32,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,153,152,154,156,160,158,159,155,173]
    largo=int(len(palabra))
    if(largo<25):
        falta=25-largo
        num=0
        final=""
        for i in range(largo-1):
            num=ord(palabra[i])+ord(palabra[i+1])
            if(num>800):
                    num=num-800
            while(num in nosirve):
                num=num+(int(num/7))

            final=final+chr(num)
        acumulado=ord(palabra[largo-1])
        for i in range(falta+1):
            if(i%2==0):
                acumulado=acumulado+7
                if(num>800):
                    num=num-800
                while(acumulado in nosirve):
                    acumulado=acumulado+(int(acumulado/7))
                final=final+chr(acumulado)
            else:
                acumulado=acumulado-5
                if(num<=0):
                    num=800+num
                while(acumulado in nosirve):
                    acumulado=acumulado+(int(acumulado/5))
                final=final+chr(acumulado)
    else:
        divisionxd=int(largo/25)
        resto=int(largo%25)
        final=""
        limit=divisionxd*25
        contador=0
        num=0
        for i in range(largo-1):
            if(i<limit):
                if(palabra[i]==' ' or palabra[i+1]==' ' ):
                    num=7+largo
                else:
                    num=ord(palabra[i])+ord(palabra[i+1])
                if(num>800):
                    num=num-800
                if(contador==divisionxd):
                    while(num in nosirve):
                        num=num+(int(num/7))
                    final=final+chr(num)
                    num=0
                    contador=0
                contador=contador+1
            else:
                 num=ord(palabra[i])+int(ord(palabra[i+1]))-int(ord(palabra[i+1])/2)
                 if(num>800):
                    num=num-800
                 while(num in nosirve):
                        num=num+(int(num/7))
        final=final+chr(num)
    print(palabra+"---------->"+final+" largo del hash "+str(len(final)))
def entropia(texto):
    base = 16 
    entropia = len(texto)*math.log(base, 2) #H = LLog2(W)
    return entropia
print('introduzca palabra para hashear')   
opcion = input()       
hash(opcion)
        