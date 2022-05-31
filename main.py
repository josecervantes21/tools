import serial
led=0

serialArduino=serial.Serial("COM3",9600)
def showMenu():
    if led==1:
        print('Menu de opciones********* ')
    else: 
        print("L encender led x salir")
while True:
    showMenu()
    opcion=input("Que deseas").upper()
    if opcion=='L':
        print(led)
        if led==1:
            led=0
            print('se apago el led')
        else:
            led=1;
            print("led encendido")
        cad=str(led)
        serialArduino.write(cad.encode('ascii'))
        print('LED')
    elif opcion=='m':
        print("Salinedo")
        break
    else:
        print("opcion no caalida")