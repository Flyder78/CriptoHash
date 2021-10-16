

import math

def hash(palabra):
    #este arreglo es porque  los caracteres con valor de Unicode que estan dentro del arreglo son caracteres invalidos o vacios que no puede mostrar python
    nosirve=[0,7,8,9,10,13,27,32,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,153,152,154,157,156,160,158,159,155,173]
    largo=int(len(palabra))
    #Este if es para cuando la palabra ingresada es menor a 25
    if(largo<25):
        falta=25-largo
        num=0
        final=""
        #el for es hasta menos 1 porque una letra se define en funcion de la siguiente
        for i in range(largo-1):
            #ord toma un caracter y me entrega su valor en Unicode
            num=ord(palabra[i])+ord(palabra[i+1])
            if(num>800):
                    num=num-800
            while(num in nosirve):
                num=num+(int(num/7))
                if(num>800):
                    num=num-800
            #chr toma un valor y me entrega su caracter en Unicode
            final=final+chr(num)
        acumulado=ord(palabra[largo-1])
        #este for es para rellenar, se toma el ultimo valor de la palabra y se empieza a rellenar segun ese valor es distitnto cuando es un valor par  o impar
        for i in range(falta+1):
            if(i%2==0):
                acumulado=acumulado+6
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
    #el else es para cuando la palabra es mayor o igual a 25
    else:
        #la division es para que el hash siempre de 25, la division me dara un numero por ejemplo 2 entonces 1 caracter del hash se calcula segun 2 caracteres de la palabra
        divisionxd=int(largo/25)
        #el resto es para calcular el ultimo caracter, este se calcula segun todos los caracteres que sobraron, el maximo que se puede son 24 caracteres 
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
def entropia():
    base = 758 
    entropia = 25*math.log(base, 2) #H = LLog2(W)
    print(entropia)
print('que quieres hacer?')
print('1.- hashear string')
print('2.- Archivo')
print('3.- Entropia')  
opcion = input()
if(opcion=='1'):
    print('ingrese palabra')
    palabra = input()
    hash(str(palabra))
if(opcion=='2'):
    contador=0
    print("ingrese el path del archivo")
    path=input()
    with open(path, 'r',errors='ignore') as log_file_fh:
                for i in log_file_fh:
                    hash(str(i))

                    
if(opcion=='3'):
    entropia()
        