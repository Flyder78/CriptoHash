
def hash(palabra):
    nosirve=[0,7,8,9,10,13,27,32,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,153,152,154,156,160,158,159,155,173]
    largo=int(len(palabra))
    if(largo<25):
        falta=25-largo
        num=0
        final=""
        for i in range(largo-1):
            num=ord(palabra[i])+ord(palabra[i+1])
            while(num in nosirve):
                num=num+(int(num/7))

            final=final+chr(num)
        acumulado=ord(palabra[largo-1])
        for i in range(falta-1):
            if(i%2==0):
                acumulado=acumulado+7
                while(acumulado in nosirve):
                    acumulado=acumulado+(int(acumulado/7))
                final=final+chr(acumulado)
            else:
                acumulado=acumulado-5
                while(acumulado in nosirve):
                    acumulado=acumulado+(int(acumulado/5))
                final=final+chr(acumulado)
    return final
palabra="holi"
print(palabra+" el hash es" +hash(palabra)+"\n")
palabra="poder"
print(palabra+" el hash es" +hash(palabra)+"\n")
palabra="aaaaaa"
print(palabra+" el hash es" +hash(palabra)+"\n")
            
            
        