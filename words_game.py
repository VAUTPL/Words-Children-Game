#############################################
# Universidad Tecnica Particular de Loja    #
#############################################
# Professor:                                #
# Rodrigo Barba        lrbarba@utpl.edu.ec  #
#############################################
# Students:                                 #
# Henry Vivanco      hpvivanco@utpl.edu.ec #
# Alberto Guarnizo   jaguarnizo4@utpl.edu.ec#
#############################################
#-----------------------------------------------------------------------------------------------------------------
#librarys
import pygame
from pygame.locals import *
import cv2
import numpy as np

#declaracion de variables e imagenes globales
cont=0
centroPantalla = (215, 80)
fel1 = cv2.imread("images/felic.png")
trist = cv2.imread("images/trist.png")
cong=0
# inicio de la funcion pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((340, 400))

def img(img1,img2,xpos,ypos):
    rows2,cols2,channels2 = img2.shape
    rows1,cols1,channels1 = img1.shape
    print (str(rows2)+'x'+str(rows1))
    aux = np.zeros((rows2, cols2, 3), dtype = "uint8")
    for i in range(rows1):
        for j in range(cols1):
            aux[xpos+i,ypos+j]=img1[i,j]
    return aux
#Incio del juego
captura = cv2.VideoCapture(0)
#Declaracion de variables para ubicacion de las imagenes en las zonas designadas
bdx=15
bdy=150
base=150
altura=150
radio=20
c_punt=[0,0,0]
l_p=10
#funcion para cargar las imagenes de la primera palabra
def CargarImagen1():
    pal1 = cv2.imread("images\ca.png")
    pal3 = cv2.imread("images/me.png")
    pal2 = cv2.imread("images/ra.png")
    pal4 = cv2.imread("images/lo.png")
    salir = cv2.imread("images\salir1.png")
    _, imagen1 = captura.read()
    # Ceamos una mascara con las direcciones de las imagenes palabra1
    up = img(pal1, imagen1, bdx - 80 + base, bdy - 50 + base)
    down = img(pal3, imagen1, bdx - 80 + base, bdy + 85 + base)
    left = img(pal2, imagen1, bdx - 80 + base, bdy - 200 + altura)
    right = img(pal4, imagen1, bdx - 80 + base, bdy + 200 + altura)
    exit = img(salir,imagen1,bdx+175+base,bdy+225+altura)
    #
    dire = cv2.add(up, down)
    dire = cv2.add(dire, left)
    dire = cv2.add(dire, right)
    dire = cv2.add(dire, exit)
    return dire
#Funcion para validar si la palabra selecciona es correcta
def ValidarPalabra(arreg, arreg2):
    x=0
    for pal in arreg:
        if (arreg[pal] != arreg2[pal]):
            x = 1
    # condicion que presenta una ventana con una cara feliz si la palabra selecccionada coincide
    # con el arreglo predefinido, espera a que presionen una tacla y carga la siguientes imagenes
    # con la siguiente palabra
    if (x==0):
        global cong
        zz=5
        print arreg2
        print "bien"
        cv2.imshow("Felicidades..:).!!", fel1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        x = 2
        cong=1
        #funcion para cargar las imagenes de la palabra 2 si la palabra anterior estuvo correctamente formada
        def CargarImagen2():
            pal1 = cv2.imread("images/bi.png")
            pal3 = cv2.imread("images/ta.png")
            pal2 = cv2.imread("images/ci.png")
            pal4 = cv2.imread("images/cle.png")
            salir = cv2.imread("images\salir1.png")
            _, imagen1 = captura.read()
            # Ceamos una mascara con las direcciones de las imagenes palabra2
            up = img(pal1, imagen1, bdx - 80 + base, bdy - 50 + base)
            down = img(pal3, imagen1, bdx - 80 + base, bdy + 85 + base)
            left = img(pal2, imagen1, bdx - 80 + base, bdy - 200 + altura)
            right = img(pal4, imagen1, bdx - 80 + base, bdy + 200 + altura)
            exit = img(salir, imagen1, bdx + 175 + base, bdy + 225 + altura)

            dire = cv2.add(up, down)
            dire = cv2.add(dire, left)
            dire = cv2.add(dire, right)
            dire = cv2.add(dire, exit)
            return dire

        # Funcion para validar si la palabra selecciona es correcta
        def ValidarPalabra2(arreg3, arreg4):
            x = 0
            for pal in arreg3:
                if (arreg3[pal] != arreg4[pal]):
                    x = 1
            # condicion que presenta una ventana con una cara feliz si la palabra fue seleccionada en el orden correcto,
            # ademas se establece un contador global que permita cargar otra palabra si la anterior fue correcta
            if (x == 0):
                global cong
                zz = 5
                print arreg4
                print "bien"
                cv2.imshow("Felicidades..:).!!", fel1)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                x = 2
                cong=2

                # funcion para cargar las imagenes de la palabra 3 si la palabra anterior estuvo correctamente formada
                def CargarImagen3():
                    pal1 = cv2.imread("images/da.png")
                    pal3 = cv2.imread("images/la.png")
                    pal2 = cv2.imread("images/sa.png")
                    pal4 = cv2.imread("images/en.png")
                    salir = cv2.imread("images\salir1.png")
                    _, imagen1 = captura.read()
                    # Ceamos una mascara con las direcciones de las imagenes palabra3
                    up = img(pal1, imagen1, bdx - 80 + base, bdy - 50 + base)
                    down = img(pal3, imagen1, bdx - 80 + base, bdy + 85 + base)
                    left = img(pal2, imagen1, bdx - 80 + base, bdy - 200 + altura)
                    right = img(pal4, imagen1, bdx - 80 + base, bdy + 200 + altura)
                    exit = img(salir, imagen1, bdx + 175 + base, bdy + 225 + altura)

                    dire = cv2.add(up, down)
                    dire = cv2.add(dire, left)
                    dire = cv2.add(dire, right)
                    dire = cv2.add(dire, exit)
                    return dire

                # Funcion para validar si la palabra selecciona es correcta
                def ValidarPalabra3(arreg5, arreg6):
                    x = 0
                    for pal in arreg5:
                        if (arreg5[pal] != arreg6[pal]):
                            x = 1
                    if (x == 0):
                        zz = 5
                        global cong
                        print arreg6
                        print "bien"
                        cv2.imshow("Felicidades..:).!!", fel1)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        x = 2
                        cong=3

                        # funcion para cargar las imagenes de la palabra 4 si la palabra anterior estuvo correctamente formada
                        def CargarImagen4():
                            pal1 = cv2.imread("images/ta.png")
                            pal3 = cv2.imread("images/se.png")
                            pal2 = cv2.imread("images/cam.png")
                            pal4 = cv2.imread("images/mi.png")
                            salir = cv2.imread("images\salir1.png")
                            _, imagen1 = captura.read()
                            # Ceamos una mascara con las direcciones de las imagenes palabra4
                            up = img(pal1, imagen1, bdx - 80 + base, bdy - 50 + base)
                            down = img(pal3, imagen1, bdx - 80 + base, bdy + 85 + base)
                            left = img(pal2, imagen1, bdx - 80 + base, bdy - 200 + altura)
                            right = img(pal4, imagen1, bdx - 80 + base, bdy + 200 + altura)
                            exit = img(salir, imagen1, bdx + 175 + base, bdy + 225 + altura)

                            dire = cv2.add(up, down)
                            dire = cv2.add(dire, left)
                            dire = cv2.add(dire, right)
                            dire = cv2.add(dire, exit)
                            return dire

                        # Funcion para validar si la palabra selecciona es correcta
                        def ValidarPalabra4(arreg7, arreg8):
                            x = 0
                            for pal in arreg7:
                                if (arreg7[pal] != arreg8[pal]):
                                    x = 1
                            # condicion que presenta una ventana con una cara feliz si la palabra selecccionada coincide
                            # con el arreglo predefinido, espera a que presionen una tacla y carga la siguientes imagenes
                            # con la siguiente palabra
                            if (x == 0):
                                zz = 5
                                global cong
                                print arreg8
                                print "bien"
                                cv2.imshow("Felicidades..:).!!", fel1)
                                cv2.waitKey(0)
                                cv2.destroyAllWindows()
                                x = 2
                                cong=4

                                # funcion para cargar las imagenes de la palabra 5 si la palabra anterior estuvo correctamente formada
                                def CargarImagen5():
                                    pal1 = cv2.imread("images/fo.png")
                                    pal3 = cv2.imread("images/te.png")
                                    pal2 = cv2.imread("images/no.png")
                                    pal4 = cv2.imread("images/le.png")
                                    salir = cv2.imread("images\salir1.png")
                                    _, imagen1 = captura.read()
                                    # Ceamos una mascara con las direcciones de las imagenes palabra5
                                    up = img(pal1, imagen1, bdx - 80 + base, bdy - 50 + base)
                                    down = img(pal3, imagen1, bdx - 80 + base, bdy + 85 + base)
                                    left = img(pal2, imagen1, bdx - 80 + base, bdy - 200 + altura)
                                    right = img(pal4, imagen1, bdx - 80 + base, bdy + 200 + altura)
                                    exit = img(salir, imagen1, bdx + 175 + base, bdy + 225 + altura)

                                    dire = cv2.add(up, down)
                                    dire = cv2.add(dire, left)
                                    dire = cv2.add(dire, right)
                                    dire = cv2.add(dire, exit)
                                    return dire

                                # Funcion para validar si la palabra selecciona es correcta
                                def ValidarPalabra5(arreg9, arreg10):
                                    x = 0
                                    #este ciclo recorre un arreglo con la palabra correcta y compara si la palabra
                                    # seleccionada coincide con el arreglo predefinido
                                    for pal in arreg9:
                                        if (arreg9[pal] != arreg10[pal]):
                                            x = 1
                                    # presenta una ventana con una caraita feliz si la palabra estuvo correcta y espera
                                    #  a que presione una tecla para continuar
                                    if (x == 0):
                                        zz = 5
                                        print arreg10
                                        print "bien"
                                        cv2.imshow("Felicidades..:).!!", fel1)
                                        cv2.waitKey(0)
                                        cv2.destroyAllWindows()
                                        x = 2
                                        exit()
                                    # presenta una ventana con una caraita triste si la palabra estuvo incorrecta
                                    # y espera a que presione una tecla para volver a cargar la misma palabra hasta que
                                    #sea formada correcta
                                    if (x == 1):
                                        x = 0
                                        print arreg10
                                        print "mal"
                                        cv2.imshow("Sigue Intentando.:(.!!", trist)
                                        cv2.waitKey(0)
                                        cv2.destroyAllWindows()
                                        cargarPalabras5()
                                # funcion que compara un contador global para cargar la palabra 4
                                if (cong == 4):
                                    def cargarPalabras5():
                                        temp1 = 0
                                        axu = 0
                                        arreg9 = {1: 'te', 2: 'le', 3: 'fo', 4: 'no'}
                                        arreg10 = {}
                                        dire = CargarImagen5()
                                        # Captura el video
                                        while True:
                                            # Captura el video y convierte RGB -> HSV
                                            _, imagen1 = captura.read()
                                            imagen1 = cv2.flip(imagen1, 1)
                                            imagen = cv2.add(imagen1, dire)

                                            cv2.rectangle(imagen, (bdy + 50 + altura, bdx - 80 + base),
                                                          (bdy - 50 + altura, bdx + base),
                                                          (255, 0, 0),
                                                          2)  # 2 ra up  150x150 pxls
                                            cv2.rectangle(imagen, (bdy + 200 + altura, bdx + base),
                                                          (bdy + 300 + altura, bdx - 80 + base),
                                                          (255, 255, 0), 2)  # 4 lo down 150x150 pxls
                                            cv2.rectangle(imagen, (bdy - 100 + altura, bdx + base),
                                                          (bdy - 200 + altura, bdx - 80 + base), (0, 0, 255),
                                                          2)  # 1 ca left 150x150 pxls
                                            cv2.rectangle(imagen, (bdy + 178 + altura, bdx + base),
                                                          (bdy + 78 + altura, bdx - 80 + base), (0, 255, 0),
                                                          2)  # 3 me right 150x150 pxls
                                            cv2.rectangle(imagen, (bdy + 325 + altura, bdx + 275 + base),
                                                          (bdy + 225 + altura, bdx + 175 + base),
                                                          (0, 0, 255), 2)  # exit 100x100 pxls

                                            hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
                                            # Creamos una mascara con el rango del color verde
                                            mask = cv2.inRange(hsv, np.array([49, 50, 50], dtype=np.uint8),
                                                               np.array([100, 255, 210], dtype=np.uint8))
                                            # Filter all noise
                                            kernel = np.ones((6, 6), np.uint8)
                                            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                                            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                                            # Difuminate the mask
                                            blur = cv2.bilateralFilter(mask, 9, 75, 75)
                                            edges = cv2.Canny(mask, 1, 2)
                                            # Encuentra el centro del objeto detectado(color verde)
                                            moments = cv2.moments(mask)
                                            area = moments['m00']
                                            event = pygame.event.poll()

                                            # Busca que el area del objeto sea mayor al pixelado descrito
                                            if (area > 200000):
                                                x = int(moments['m10'] / moments['m00'])
                                                y = int(moments['m01'] / moments['m00'])
                                                # Dibuja el centro del objeto
                                                cv2.circle(imagen, (x, y), radio, (c_punt), 5)
                                                cv2.line(imagen, (x, y + radio - l_p), (x, y + radio + l_p), (c_punt),
                                                         5)
                                                cv2.line(imagen, (x, y - radio - l_p), (x, y - radio + l_p), (c_punt),
                                                         5)
                                                cv2.line(imagen, (x + radio - l_p, y), (x + radio + l_p, y), (c_punt),
                                                         5)
                                                cv2.line(imagen, (x - radio - l_p, y), (x - radio + l_p, y), (c_punt),
                                                         5)
                                                # variable contiene la longitud del arreglo
                                                aaa = len(arreg10)
                                                if (aaa == 4):
                                                    aaa = 0
                                                    # Enviamos los arreglos 9 y 10 a la funcion de validar
                                                    ValidarPalabra5(arreg9, arreg10)
                                                # Detectamos si el color esta en una region en especifico y comparamos
                                                # si dicho valor ya ha sido asignado anteriormente
                                                if (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (
                                                                bdy - 50 + altura) and x <= (
                                                                bdy + 50 + altura)):
                                                    for pal in arreg10:
                                                        if (arreg10[pal] == 'fo'):
                                                            temp1 = 1
                                                        elif (temp1 == 1):
                                                            ff = 3
                                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                                    # actualiza la imagen
                                                    if (temp1 == 0):
                                                        axu += 1
                                                        arreg10[axu] = "fo"
                                                        cv2.putText(imagen, arreg10[axu], (x, y),
                                                                    cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                                    0, 0)
                                                        act = cv2.imread("images/act.png")
                                                        _, imagen1 = captura.read()
                                                        up = img(act, imagen1, bdx - 80 + base, bdy - 50 + base)
                                                        dire = cv2.add(dire, up)
                                                    temp1 = 0
                                                # Detectamos si el color esta en una region en especifico y comparamos
                                                # si dicho valor ya ha sido asignado anteriormente
                                                elif (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (
                                                                bdy + 200 + altura) and x <= (
                                                                bdy + 300 + altura)):
                                                    for pal in arreg10:
                                                        if (arreg10[pal] == 'le'):
                                                            temp1 = 1
                                                        elif (temp1 == 1):
                                                            ff = 3
                                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                                    # actualiza la imagen
                                                    if (temp1 == 0):
                                                        axu += 1
                                                        arreg10[axu] = "le"
                                                        cv2.putText(imagen, arreg10[axu], (x, y),
                                                                    cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                                    0, 0)
                                                        act = cv2.imread("images/act.png")
                                                        _, imagen1 = captura.read()
                                                        down = img(act, imagen1, bdx - 80 + base, bdy + 200 + altura)
                                                        dire = cv2.add(dire, down)
                                                    temp1 = 0
                                                # Detectamos si el color esta en una region en especifico y comparamos
                                                # si dicho valor ya ha sido asignado anteriormente
                                                elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (
                                                                bdy - 200 + altura) and x < (
                                                                bdy - 100 + altura)):
                                                    for pal in arreg10:
                                                        if (arreg10[pal] == 'no'):
                                                            temp1 = 1
                                                        elif (temp1 == 1):
                                                            ff = 3
                                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                                    # actualiza la imagen
                                                    if (temp1 == 0):
                                                        axu += 1
                                                        arreg10[axu] = "no"
                                                        cv2.putText(imagen, arreg10[axu], (x, y),
                                                                    cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                                    0, 0)
                                                        act = cv2.imread("images/act.png")
                                                        _, imagen1 = captura.read()
                                                        left = img(act, imagen1, bdx - 80 + base, bdy - 200 + altura)
                                                        dire = cv2.add(dire, left)
                                                    temp1 = 0
                                                # Detectamos si el color esta en una region en especifico y comparamos
                                                # si dicho valor ya ha sido asignado anteriormente
                                                elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (
                                                                bdy + 75 + altura) and x < (
                                                                bdy + 175 + altura)):
                                                    for pal in arreg10:
                                                        if (arreg10[pal] == 'te'):
                                                            temp1 = 1
                                                        elif (temp1 == 1):
                                                            ff = 3
                                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                                    # actualiza la imagen
                                                    if (temp1 == 0):
                                                        axu += 1
                                                        arreg10[axu] = "te"
                                                        cv2.putText(imagen, arreg10[axu], (x, y),
                                                                    cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                                    0, 0)
                                                        act = cv2.imread("images/act.png")
                                                        _, imagen1 = captura.read()
                                                        right = img(act, imagen1, bdx - 80 + base, bdy + 85 + base)
                                                        dire = cv2.add(dire, right)
                                                    temp1 = 0
                                                # Si el color esta en esta region cerramos la ventana del juego
                                                elif (y > (bdx + 175 + base) and y < (bdx + 275 + base) and x > (
                                                                bdy + 225 + altura) and x < (
                                                                bdy + 325 + altura)):
                                                    cv2.putText(imagen, "SALIR", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                                0, 0)
                                                    pygame.event.post(pygame.event.Event(QUIT))
                                                    break
                                            # Muestra el video en una ventana
                                            cv2.imshow('Camara', imagen)
                                            tecla = cv2.waitKey(5) & 0xFF
                                            if tecla == 27:
                                                break
                                            # Funcion flip para que siga al lado correcto el color (para evitar que la
                                            # imagen sea como espejo)
                                            pygame.display.flip()
                                            clock.tick(12)
                                    # llamamos a la funcion cargar palabras
                                    cargarPalabras5()
                                    cv2.destroyAllWindows()
                            # presenta una ventana con una caraita triste si la palabra estuvo incorrecta
                            # y espera a que presione una tecla para volver a cargar la misma palabra hasta que
                            # sea formada correcta
                            if (x == 1):
                                x = 0
                                print arreg8
                                print "mal"
                                cv2.imshow("Sigue Intentando.:(.!!", trist)
                                cv2.waitKey(0)
                                cv2.destroyAllWindows()
                                cargarPalabras4()

                        # funcion que compara un contador global para cargar la palabra 3
                        if (cong == 3):
                            def cargarPalabras4():
                                temp1 = 0
                                axu = 0
                                arreg7 = {1: 'ca', 2: 'mi', 3: 'se', 4: 'ta'}
                                arreg8 = {}
                                dire = CargarImagen4()
                                # captura el video
                                while True:
                                    # Captura el video y convierte RGB -> HSV
                                    _, imagen1 = captura.read()
                                    imagen1 = cv2.flip(imagen1, 1)
                                    imagen = cv2.add(imagen1, dire)

                                    cv2.rectangle(imagen, (bdy + 50 + altura, bdx - 80 + base),
                                                  (bdy - 50 + altura, bdx + base),
                                                  (255, 0, 0),
                                                  2)  # 2 ra up  150x150 pxls
                                    cv2.rectangle(imagen, (bdy + 200 + altura, bdx + base),
                                                  (bdy + 300 + altura, bdx - 80 + base),
                                                  (255, 255, 0), 2)  # 4 lo down 150x150 pxls
                                    cv2.rectangle(imagen, (bdy - 100 + altura, bdx + base),
                                                  (bdy - 200 + altura, bdx - 80 + base), (0, 0, 255),
                                                  2)  # 1 ca left 150x150 pxls
                                    cv2.rectangle(imagen, (bdy + 178 + altura, bdx + base),
                                                  (bdy + 78 + altura, bdx - 80 + base), (0, 255, 0),
                                                  2)  # 3 me right 150x150 pxls
                                    cv2.rectangle(imagen, (bdy + 325 + altura, bdx + 275 + base),
                                                  (bdy + 225 + altura, bdx + 175 + base),
                                                  (0, 0, 255), 2)  # exit 100x100 pxls

                                    hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
                                    # Creamos una mascara con el rango de color verde
                                    mask = cv2.inRange(hsv, np.array([49, 50, 50], dtype=np.uint8),
                                                       np.array([100, 255, 210], dtype=np.uint8))
                                    # Filter all noise
                                    kernel = np.ones((6, 6), np.uint8)
                                    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                                    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                                    # Difuminate the mask
                                    blur = cv2.bilateralFilter(mask, 9, 75, 75)
                                    edges = cv2.Canny(mask, 1, 2)
                                    # Encuentra el centro del objeto detectado(color verde)
                                    moments = cv2.moments(mask)
                                    area = moments['m00']
                                    event = pygame.event.poll()

                                    # Busca que el area del objeto sea mayor al pixelado descrito
                                    if (area > 200000):
                                        x = int(moments['m10'] / moments['m00'])
                                        y = int(moments['m01'] / moments['m00'])
                                        # Dibuja el centro del objeto
                                        cv2.circle(imagen, (x, y), radio, (c_punt), 5)
                                        cv2.line(imagen, (x, y + radio - l_p), (x, y + radio + l_p), (c_punt), 5)
                                        cv2.line(imagen, (x, y - radio - l_p), (x, y - radio + l_p), (c_punt), 5)
                                        cv2.line(imagen, (x + radio - l_p, y), (x + radio + l_p, y), (c_punt), 5)
                                        cv2.line(imagen, (x - radio - l_p, y), (x - radio + l_p, y), (c_punt), 5)
                                        # variable contiene la longitud del arreglo
                                        aaa = len(arreg8)
                                        if (aaa == 4):
                                            aaa = 0
                                            # Enviamos los arreglos 7 y 8 a la funcion de validar
                                            ValidarPalabra4(arreg7, arreg8)
                                        # Detectamos si el color esta en una region en especifico y comparamos
                                        # si dicho valor ya ha sido asignado anteriormente
                                        if (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (
                                                bdy - 50 + altura) and x <= (
                                                        bdy + 50 + altura)):
                                            for pal in arreg8:
                                                if (arreg8[pal] == 'ta'):
                                                    temp1 = 1
                                                elif (temp1 == 1):
                                                    ff = 3
                                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                            # actualiza la imagen
                                            if (temp1 == 0):
                                                axu += 1
                                                arreg8[axu] = "ta"
                                                cv2.putText(imagen, arreg8[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                            0, 0)
                                                act = cv2.imread("images/act.png")
                                                _, imagen1 = captura.read()
                                                up = img(act, imagen1, bdx - 80 + base, bdy - 50 + base)
                                                dire = cv2.add(dire, up)
                                            temp1 = 0
                                        # Detectamos si el color esta en una region en especifico y comparamos
                                        # si dicho valor ya ha sido asignado anteriormente
                                        elif (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (
                                                        bdy + 200 + altura) and x <= (
                                                        bdy + 300 + altura)):
                                            for pal in arreg8:
                                                if (arreg8[pal] == 'mi'):
                                                    temp1 = 1
                                                elif (temp1 == 1):
                                                    ff = 3
                                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                            # actualiza la imagen
                                            if (temp1 == 0):
                                                axu += 1
                                                arreg8[axu] = "mi"
                                                cv2.putText(imagen, arreg8[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                            0, 0)
                                                act = cv2.imread("images/act.png")
                                                _, imagen1 = captura.read()
                                                down = img(act, imagen1, bdx - 80 + base, bdy + 200 + altura)
                                                dire = cv2.add(dire, down)
                                            temp1 = 0
                                        # Detectamos si el color esta en una region en especifico y comparamos
                                        # si dicho valor ya ha sido asignado anteriormente
                                        elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (
                                                bdy - 200 + altura) and x < (
                                                        bdy - 100 + altura)):
                                            for pal in arreg8:
                                                if (arreg8[pal] == 'ca'):
                                                    temp1 = 1
                                                elif (temp1 == 1):
                                                    ff = 3
                                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                            # actualiza la imagen
                                            if (temp1 == 0):
                                                axu += 1
                                                arreg8[axu] = "ca"
                                                cv2.putText(imagen, arreg8[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                            0, 0)
                                                act = cv2.imread("images/act.png")
                                                _, imagen1 = captura.read()
                                                left = img(act, imagen1, bdx - 80 + base, bdy - 200 + altura)
                                                dire = cv2.add(dire, left)
                                            temp1 = 0
                                        # Detectamos si el color esta en una region en especifico y comparamos
                                        # si dicho valor ya ha sido asignado anteriormente
                                        elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (
                                                bdy + 75 + altura) and x < (
                                                        bdy + 175 + altura)):
                                            for pal in arreg8:
                                                if (arreg8[pal] == 'se'):
                                                    temp1 = 1
                                                elif (temp1 == 1):
                                                    ff = 3
                                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                            # actualiza la imagen
                                            if (temp1 == 0):
                                                axu += 1
                                                arreg8[axu] = "se"
                                                cv2.putText(imagen, arreg8[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,
                                                            0, 0)
                                                act = cv2.imread("images/act.png")
                                                _, imagen1 = captura.read()
                                                right = img(act, imagen1, bdx - 80 + base, bdy + 85 + base)
                                                dire = cv2.add(dire, right)
                                            temp1 = 0
                                        # Si el color esta en esta region cerramos la ventana del juego
                                        elif (y > (bdx + 175 + base) and y < (bdx + 275 + base) and x > (
                                                        bdy + 225 + altura) and x < (
                                                        bdy + 325 + altura)):
                                            cv2.putText(imagen, "SALIR", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                            pygame.event.post(pygame.event.Event(QUIT))
                                            break
                                    # Muestra el video en una ventana
                                    cv2.imshow('Camara', imagen)
                                    tecla = cv2.waitKey(5) & 0xFF
                                    if tecla == 27:
                                        break
                                    # Funcion flip para que siga al lado correcto el color (para evitar que la
                                    # imagen sea como espejo)
                                    pygame.display.flip()
                                    clock.tick(12)
                            # llamamos a la funcion cargar palabras
                            cargarPalabras4()
                            cv2.destroyAllWindows()
                    # presenta una ventana con una caraita triste si la palabra estuvo incorrecta
                    # y espera a que presione una tecla para volver a cargar la misma palabra hasta que
                    # sea formada correcta
                    if (x == 1):
                        x = 0
                        print arreg6
                        print "mal"
                        cv2.imshow("Sigue Intentando.:(.!!", trist)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        cong=2
                        cargarPalabras3()
                # funcion que compara un contador global para cargar la palabra 4
                if (cong == 2):
                    def cargarPalabras3():
                        temp1 = 0
                        axu = 0
                        arreg5 = {1: 'en', 2: 'sa', 3: 'la', 4: 'da'}
                        arreg6 = {}
                        dire = CargarImagen3()
                        # capture the video
                        while True:

                            # Captue video and convert RGB -> HSV
                            _, imagen1 = captura.read()
                            imagen1 = cv2.flip(imagen1, 1)
                            imagen = cv2.add(imagen1, dire)

                            cv2.rectangle(imagen, (bdy + 50 + altura, bdx - 80 + base), (bdy - 50 + altura, bdx + base),
                                          (255, 0, 0),
                                          2)  # 2 ra up  150x150 pxls
                            cv2.rectangle(imagen, (bdy + 200 + altura, bdx + base),
                                          (bdy + 300 + altura, bdx - 80 + base),
                                          (255, 255, 0), 2)  # 4 lo down 150x150 pxls
                            cv2.rectangle(imagen, (bdy - 100 + altura, bdx + base),
                                          (bdy - 200 + altura, bdx - 80 + base), (0, 0, 255),
                                          2)  # 1 ca left 150x150 pxls
                            cv2.rectangle(imagen, (bdy + 178 + altura, bdx + base),
                                          (bdy + 78 + altura, bdx - 80 + base), (0, 255, 0),
                                          2)  # 3 me right 150x150 pxls
                            cv2.rectangle(imagen, (bdy + 325 + altura, bdx + 275 + base),
                                          (bdy + 225 + altura, bdx + 175 + base),
                                          (0, 0, 255), 2)  # exit 100x100 pxls

                            hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
                            # Creamos una mascara con el rango de color verde
                            mask = cv2.inRange(hsv, np.array([49, 50, 50], dtype=np.uint8),
                                               np.array([100, 255, 210], dtype=np.uint8))
                            # Filter all noise
                            kernel = np.ones((6, 6), np.uint8)
                            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                            # Difuminate the mask
                            blur = cv2.bilateralFilter(mask, 9, 75, 75)
                            edges = cv2.Canny(mask, 1, 2)
                            # Encuentra el centro del objeto detectado(color verde)
                            moments = cv2.moments(mask)
                            area = moments['m00']
                            event = pygame.event.poll()

                            # Busca que el area del objeto sea mayor al pixelado descrito
                            if (area > 200000):
                                x = int(moments['m10'] / moments['m00'])
                                y = int(moments['m01'] / moments['m00'])
                                # Dibuja el centro del objeto
                                cv2.circle(imagen, (x, y), radio, (c_punt), 5)
                                cv2.line(imagen, (x, y + radio - l_p), (x, y + radio + l_p), (c_punt), 5)
                                cv2.line(imagen, (x, y - radio - l_p), (x, y - radio + l_p), (c_punt), 5)
                                cv2.line(imagen, (x + radio - l_p, y), (x + radio + l_p, y), (c_punt), 5)
                                cv2.line(imagen, (x - radio - l_p, y), (x - radio + l_p, y), (c_punt), 5)
                                # variable contiene la longitud del arreglo
                                aaa = len(arreg6)
                                if (aaa == 4):
                                    aaa = 0
                                    # Enviamos los arreglos 5 y 6 a la funcion de validar
                                    ValidarPalabra3(arreg5, arreg6)
                                # Detectamos si el color esta en una region en especifico y comparamos
                                # si dicho valor ya ha sido asignado anteriormente
                                if (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (bdy - 50 + altura) and x <= (
                                                bdy + 50 + altura)):
                                    for pal in arreg6:
                                        if (arreg6[pal] == 'da'):
                                            temp1 = 1
                                        elif (temp1 == 1):
                                            ff = 3
                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                    # actualiza la imagen
                                    if (temp1 == 0):
                                        axu += 1
                                        arreg6[axu] = "da"
                                        cv2.putText(imagen, arreg6[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                        act = cv2.imread("images/act.png")
                                        _, imagen1 = captura.read()
                                        up = img(act, imagen1, bdx - 80 + base, bdy - 50 + base)
                                        dire = cv2.add(dire, up)
                                    temp1 = 0
                                # Detectamos si el color esta en una region en especifico y comparamos
                                # si dicho valor ya ha sido asignado anteriormente
                                elif (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (
                                        bdy + 200 + altura) and x <= (
                                                bdy + 300 + altura)):
                                    for pal in arreg6:
                                        if (arreg6[pal] == 'en'):
                                            temp1 = 1
                                        elif (temp1 == 1):
                                            ff = 3
                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                    # actualiza la imagen
                                    if (temp1 == 0):
                                        axu += 1
                                        arreg6[axu] = "en"
                                        cv2.putText(imagen, arreg6[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                        act = cv2.imread("images/act.png")
                                        _, imagen1 = captura.read()
                                        down = img(act, imagen1, bdx - 80 + base, bdy + 200 + altura)
                                        dire = cv2.add(dire, down)
                                    temp1 = 0
                                # Detectamos si el color esta en una region en especifico y comparamos
                                # si dicho valor ya ha sido asignado anteriormente
                                elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (bdy - 200 + altura) and x < (
                                                bdy - 100 + altura)):
                                    for pal in arreg6:
                                        if (arreg6[pal] == 'sa'):
                                            temp1 = 1
                                        elif (temp1 == 1):
                                            ff = 3
                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                    # actualiza la imagen
                                    if (temp1 == 0):
                                        axu += 1
                                        arreg6[axu] = "sa"
                                        cv2.putText(imagen, arreg6[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                        act = cv2.imread("images/act.png")
                                        _, imagen1 = captura.read()
                                        left = img(act, imagen1, bdx - 80 + base, bdy - 200 + altura)
                                        dire = cv2.add(dire, left)
                                    temp1 = 0
                                # Detectamos si el color esta en una region en especifico y comparamos
                                # si dicho valor ya ha sido asignado anteriormente
                                elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (bdy + 75 + altura) and x < (
                                                bdy + 175 + altura)):
                                    for pal in arreg6:
                                        if (arreg6[pal] == 'la'):
                                            temp1 = 1
                                        elif (temp1 == 1):
                                            ff = 3
                                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                                    # actualiza la imagen
                                    if (temp1 == 0):
                                        axu += 1
                                        arreg6[axu] = "la"
                                        cv2.putText(imagen, arreg6[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                        act = cv2.imread("images/act.png")
                                        _, imagen1 = captura.read()
                                        right = img(act, imagen1, bdx - 80 + base, bdy + 85 + base)
                                        dire = cv2.add(dire, right)
                                    temp1 = 0
                                # Si el color esta en esta region cerramos la ventana del juego
                                elif (y > (bdx + 175 + base) and y < (bdx + 275 + base) and x > (
                                        bdy + 225 + altura) and x < (
                                                bdy + 325 + altura)):
                                    cv2.putText(imagen, "SALIR", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                    pygame.event.post(pygame.event.Event(QUIT))
                                    break
                            # Muestra el video en una ventana
                            cv2.imshow('Camara', imagen)
                            tecla = cv2.waitKey(5) & 0xFF
                            if tecla == 27:
                                break
                            # Funcion flip para que siga al lado correcto el color (para evitar que la
                            # imagen sea como espejo)
                            pygame.display.flip()
                            clock.tick(12)
                    # llamamos a la funcion cargar palabras
                    cargarPalabras3()
                    cv2.destroyAllWindows()
            # presenta una ventana con una caraita triste si la palabra estuvo incorrecta
            # y espera a que presione una tecla para volver a cargar la misma palabra hasta que
            # sea formada correcta
            if (x == 1):
                x = 0
                print arreg4
                print "mal"
                cv2.imshow("Sigue Intentando.:(.!!", trist)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cargarPalabras2()

        # funcion que compara un contador global para cargar la palabra 2
        if (cong == 1):
            def cargarPalabras2():
                temp1 = 0
                axu = 0
                arreg3 = {1: 'bi', 2: 'ci', 3: 'cle', 4: 'ta'}
                arreg4 = {}
                dire = CargarImagen2()
                # captura el video
                while True:
                    # Captura el video y convierte RGB -> HSV
                    _, imagen1 = captura.read()
                    imagen1 = cv2.flip(imagen1, 1)
                    imagen = cv2.add(imagen1, dire)

                    cv2.rectangle(imagen, (bdy + 50 + altura, bdx - 80 + base), (bdy - 50 + altura, bdx + base),
                                  (255, 0, 0),
                                  2)  # 2 ra up  150x150 pxls
                    cv2.rectangle(imagen, (bdy + 200 + altura, bdx + base), (bdy + 300 + altura, bdx - 80 + base),
                                  (255, 255, 0), 2)  # 4 lo down 150x150 pxls
                    cv2.rectangle(imagen, (bdy - 100 + altura, bdx + base), (bdy - 200 + altura, bdx - 80 + base),
                                  (0, 0, 255),
                                  2)  # 1 ca left 150x150 pxls
                    cv2.rectangle(imagen, (bdy + 178 + altura, bdx + base), (bdy + 78 + altura, bdx - 80 + base),
                                  (0, 255, 0),
                                  2)  # 3 me right 150x150 pxls
                    cv2.rectangle(imagen, (bdy + 325 + altura, bdx + 275 + base),
                                  (bdy + 225 + altura, bdx + 175 + base),
                                  (0, 0, 255), 2)  # exit 100x100 pxls

                    hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
                    # Creamos una mascara con el rango de color verde
                    mask = cv2.inRange(hsv, np.array([49, 50, 50], dtype=np.uint8),
                                       np.array([100, 255, 210], dtype=np.uint8))
                    # Filter all noise
                    kernel = np.ones((6, 6), np.uint8)
                    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                    # Difuminate the mask
                    blur = cv2.bilateralFilter(mask, 9, 75, 75)
                    edges = cv2.Canny(mask, 1, 2)
                    # Encuentra el centro del objeto detectado(color verde)
                    moments = cv2.moments(mask)
                    area = moments['m00']
                    event = pygame.event.poll()

                    # Busca que el area del objeto sea mayor al pixelado descrito
                    if (area > 200000):
                        x = int(moments['m10'] / moments['m00'])
                        y = int(moments['m01'] / moments['m00'])
                        # Dibuja el centro del objeto
                        cv2.circle(imagen, (x, y), radio, (c_punt), 5)
                        cv2.line(imagen, (x, y + radio - l_p), (x, y + radio + l_p), (c_punt), 5)
                        cv2.line(imagen, (x, y - radio - l_p), (x, y - radio + l_p), (c_punt), 5)
                        cv2.line(imagen, (x + radio - l_p, y), (x + radio + l_p, y), (c_punt), 5)
                        cv2.line(imagen, (x - radio - l_p, y), (x - radio + l_p, y), (c_punt), 5)
                        # variable contiene la longitud del arreglo
                        aaa = len(arreg4)
                        if (aaa == 4):
                            aaa = 0
                            # Enviamos los arreglos 3 y 4 a la funcion de validar
                            ValidarPalabra2(arreg3, arreg4)

                        # Detectamos si el color esta en una region en especifico y comparamos
                        # si dicho valor ya ha sido asignado anteriormente
                        if (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (bdy - 50 + altura) and x <= (
                                        bdy + 50 + altura)):
                            for pal in arreg4:
                                if (arreg4[pal] == 'bi'):
                                    temp1 = 1
                                elif (temp1 == 1):
                                    ff = 3
                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                            # actualiza la imagen
                            if (temp1 == 0):
                                axu += 1
                                arreg4[axu] = "bi"
                                cv2.putText(imagen, arreg4[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                act = cv2.imread("images/act.png")
                                _, imagen1 = captura.read()
                                up = img(act, imagen1, bdx - 80 + base, bdy - 50 + base)
                                dire = cv2.add(dire, up)
                            temp1 = 0
                        # Detectamos si el color esta en una region en especifico y comparamos
                        # si dicho valor ya ha sido asignado anteriormente
                        elif (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (bdy + 200 + altura) and x <= (
                                        bdy + 300 + altura)):
                            for pal in arreg4:
                                if (arreg4[pal] == 'cle'):
                                    temp1 = 1
                                elif (temp1 == 1):
                                    ff = 3
                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                            # actualiza la imagen
                            if (temp1 == 0):
                                axu += 1
                                arreg4[axu] = "cle"
                                cv2.putText(imagen, arreg4[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                act = cv2.imread("images/act.png")
                                _, imagen1 = captura.read()
                                down = img(act, imagen1, bdx - 80 + base, bdy + 200 + altura)
                                dire = cv2.add(dire, down)
                            temp1 = 0
                        # Detectamos si el color esta en una region en especifico y comparamos
                        # si dicho valor ya ha sido asignado anteriormente
                        elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (bdy - 200 + altura) and x < (
                                        bdy - 100 + altura)):
                            for pal in arreg4:
                                if (arreg4[pal] == 'ci'):
                                    temp1 = 1
                                elif (temp1 == 1):
                                    ff = 3
                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                            # actualiza la imagen
                            if (temp1 == 0):
                                axu += 1
                                # sum += 1
                                arreg4[axu] = "ci"
                                cv2.putText(imagen, arreg4[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                act = cv2.imread("images/act.png")
                                _, imagen1 = captura.read()
                                left = img(act, imagen1, bdx - 80 + base, bdy - 200 + altura)
                                dire = cv2.add(dire, left)
                            temp1 = 0
                        # Detectamos si el color esta en una region en especifico y comparamos
                        # si dicho valor ya ha sido asignado anteriormente
                        elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (bdy + 75 + altura) and x < (
                                        bdy + 175 + altura)):
                            for pal in arreg4:
                                if (arreg4[pal] == 'ta'):
                                    temp1 = 1
                                elif (temp1 == 1):
                                    ff = 3
                            # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                            # actualiza la imagen
                            if (temp1 == 0):
                                axu += 1
                                # sum += 1
                                arreg4[axu] = "ta"
                                cv2.putText(imagen, arreg4[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                                act = cv2.imread("images/act.png")
                                _, imagen1 = captura.read()
                                right = img(act, imagen1, bdx - 80 + base, bdy + 85 + base)
                                dire = cv2.add(dire, right)
                            temp1 = 0
                        # Si el color esta en esta region cerramos la ventana del juego
                        elif (y > (bdx + 175 + base) and y < (bdx + 275 + base) and x > (bdy + 225 + altura) and x < (
                                        bdy + 325 + altura)):
                            cv2.putText(imagen, "SALIR", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                            pygame.event.post(pygame.event.Event(QUIT))
                            break

                     # Muestra el video en una ventana
                    cv2.imshow('Camara', imagen)
                    tecla = cv2.waitKey(5) & 0xFF
                    if tecla == 27:
                        break
                    # Funcion flip para que siga al lado correcto el color (para evitar que la
                    # imagen sea como espejo)
                    pygame.display.flip()
                    clock.tick(12)

            # llamamos a la funcion cargar palabras
            cargarPalabras2()
            cv2.destroyAllWindows()
    # presenta una ventana con una caraita triste si la palabra estuvo incorrecta
    # y espera a que presione una tecla para volver a cargar la misma palabra hasta que
    # sea formada correcta
    if (x==1):
        x=0
        print arreg2
        print "mal"
        cv2.imshow("Sigue Intentando.:(.!!", trist)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cargarPalabras()
# funcion que compara un contador global para cargar la palabra 2
if(cong==0):
    def cargarPalabras():
        temp1 = 0
        axu = 0
        arreg = {1: 'ca', 2: 'ra', 3: 'me', 4: 'lo'}
        arreg2 = {}
        dire = CargarImagen1()
        # captura el video
        while True:
            # Captura el video y convierte RGB -> HSV
            _, imagen1 = captura.read()
            imagen1 = cv2.flip(imagen1, 1)
            imagen = cv2.add(imagen1, dire)

            cv2.rectangle(imagen, (bdy + 50 + altura, bdx - 80 + base), (bdy - 50 + altura, bdx + base), (255, 0, 0),
                          2)  # 2 ra up  150x150 pxls
            cv2.rectangle(imagen, (bdy + 200 + altura, bdx + base), (bdy + 300 + altura, bdx - 80 + base),
                          (255, 255, 0), 2)  # 4 lo down 150x150 pxls
            cv2.rectangle(imagen, (bdy - 100 + altura, bdx + base), (bdy - 200 + altura, bdx - 80 + base), (0, 0, 255),
                          2)  # 1 ca left 150x150 pxls
            cv2.rectangle(imagen, (bdy + 178 + altura, bdx + base), (bdy + 78 + altura, bdx - 80 + base), (0, 255, 0),
                          2)  # 3 me right 150x150 pxls
            cv2.rectangle(imagen, (bdy + 325 + altura, bdx + 275 + base), (bdy + 225 + altura, bdx + 175 + base),
                          (0, 0, 255), 2)  # exit 100x100 pxls

            hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
            # Creamos una mascara con el rango de color verde
            mask = cv2.inRange(hsv, np.array([49, 50, 50], dtype=np.uint8), np.array([100, 255, 210], dtype=np.uint8))
            # Filter all noise
            kernel = np.ones((6, 6), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            # Difuminate the mask
            blur = cv2.bilateralFilter(mask, 9, 75, 75)
            edges = cv2.Canny(mask, 1, 2)
            # Encuentra el centro del objeto detectado(color verde)
            moments = cv2.moments(mask)
            area = moments['m00']
            event = pygame.event.poll()

            # Busca que el area del objeto sea mayor al pixelado descrito
            if (area > 200000):
                x = int(moments['m10'] / moments['m00'])
                y = int(moments['m01'] / moments['m00'])
                # Dibuja el centro del objeto
                cv2.circle(imagen, (x, y), radio, (c_punt), 5)
                cv2.line(imagen, (x, y + radio - l_p), (x, y + radio + l_p), (c_punt), 5)
                cv2.line(imagen, (x, y - radio - l_p), (x, y - radio + l_p), (c_punt), 5)
                cv2.line(imagen, (x + radio - l_p, y), (x + radio + l_p, y), (c_punt), 5)
                cv2.line(imagen, (x - radio - l_p, y), (x - radio + l_p, y), (c_punt), 5)
                # variable contiene la longitud del arreglo
                aaa = len(arreg2)
                if (aaa == 4):
                    aaa = 0
                    # Enviamos los arreglos 3 y 4 a la funcion de validar
                    ValidarPalabra(arreg, arreg2)
                # Detectamos si el color esta en una region en especifico y comparamos
                # si dicho valor ya ha sido asignado anteriormente
                if (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (bdy - 50 + altura) and x <= (
                        bdy + 50 + altura)):
                    for pal in arreg2:
                        if (arreg2[pal] == 'ca'):
                            temp1 = 1
                        elif (temp1 == 1):
                            ff=3
                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                    # actualiza la imagen
                    if (temp1 == 0):
                        axu += 1
                        # sum+=1
                        arreg2[axu] = "ca"
                        cv2.putText(imagen, arreg2[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                        act = cv2.imread("images/act.png")
                        _, imagen1 = captura.read()
                        up = img(act, imagen1, bdx - 80 + base, bdy - 50 + base)
                        dire = cv2.add(dire, up)
                    temp1 = 0
                # Detectamos si el color esta en una region en especifico y comparamos
                # si dicho valor ya ha sido asignado anteriormente
                elif (y >= (bdx - 80 + base) and y <= (bdx + base) and x >= (bdy + 200 + altura) and x <= (
                        bdy + 300 + altura)):
                    for pal in arreg2:
                        if (arreg2[pal] == 'lo'):
                            temp1 = 1
                        elif (temp1 == 1):
                            ff = 3
                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                    # actualiza la imagen
                    if (temp1 == 0):
                        axu += 1
                        # sum += 1
                        arreg2[axu] = "lo"
                        cv2.putText(imagen, arreg2[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                        act = cv2.imread("images/act.png")
                        _, imagen1 = captura.read()
                        down = img(act, imagen1, bdx - 80 + base, bdy + 200 + altura)
                        dire = cv2.add(dire, down)
                    temp1 = 0
                # Detectamos si el color esta en una region en especifico y comparamos
                # si dicho valor ya ha sido asignado anteriormente
                elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (bdy - 200 + altura) and x < (
                        bdy - 100 + altura)):
                    for pal in arreg2:
                        if (arreg2[pal] == 'ra'):
                            temp1 = 1
                        elif (temp1 == 1):
                            ff = 3
                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                    # actualiza la imagen
                    if (temp1 == 0):
                        axu += 1
                        # sum += 1
                        arreg2[axu] = "ra"
                        cv2.putText(imagen, arreg2[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                        act = cv2.imread("images/act.png")
                        _, imagen1 = captura.read()
                        left = img(act, imagen1, bdx - 80 + base, bdy - 200 + altura)
                        dire = cv2.add(dire, left)
                    temp1 = 0
                # Detectamos si el color esta en una region en especifico y comparamos
                # si dicho valor ya ha sido asignado anteriormente
                elif (y > (bdx - 80 + base) and y < (bdx + base) and x > (bdy + 75 + altura) and x < (
                        bdy + 175 + altura)):
                    for pal in arreg2:
                        if (arreg2[pal] == 'me'):
                            temp1 = 1
                        elif (temp1 == 1):
                            ff = 3
                    # si no ha sido asignado anteriormente lo guarda en dicho arreglo y
                    # actualiza la imagen
                    if (temp1 == 0):
                        axu += 1
                        arreg2[axu] = "me"
                        cv2.putText(imagen, arreg2[axu], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                        act = cv2.imread("images/act.png")
                        _, imagen1 = captura.read()
                        right = img(act, imagen1, bdx - 80 + base, bdy + 85 + base)
                        dire = cv2.add(dire, right)
                    temp1 = 0
                # Si el color esta en esta region cerramos la ventana del juego
                elif (y > (bdx + 175 + base) and y < (bdx + 275 + base) and x > (bdy + 225 + altura) and x < (
                        bdy + 325 + altura)):
                    cv2.putText(imagen, "SALIR", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0, 0, 0)
                    pygame.event.post(pygame.event.Event(QUIT))
                    break
            # Muestra el video en una ventana
            cv2.imshow('Camara', imagen)
            tecla = cv2.waitKey(5) & 0xFF
            if tecla == 27:
                break
            # Funcion flip para que siga al lado correcto el color (para evitar que la
            # imagen sea como espejo)
            pygame.display.flip()
            clock.tick(12)
    # llamamos a la funcion cargar palabras
    cargarPalabras()
    cv2.destroyAllWindows()