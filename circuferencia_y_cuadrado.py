# integrantes:                          # pygame es la libreria la utilizamos para haer el dibujo de la diana, pero devido a que usamos un radio muy alto no logramos
#   Carlos Quinteros  RUT:20.871.229-2  #hacer que el dibujo quepa dentro de la pantalla, si usted desea probar el dibujo ponga el radio en 800 y saque de comentario el codgio que diga
#   Leonardo Solis RUT:20.580.840-k     #parte del dibujo, le aviso de ante mano que si hace esto la aproximacion de PI no se lograra
# seccion: 411 
#---------------------------------------------------------------------                           
#NOTA MUY IMPORTANTE: se demora en compilar, por favor tenga paciencia
#---------------------------------------------------------------------
import random   #libreria utilizada para generar los puntos aleatorios
import math      #libreria utlizada para sacar laa raiz
import matplotlib.pyplot as plt #libreria utilizada para mostrar el grafico
import pygame                         
import pandas as pd         #libreria utilizada para mostrar los datos de forma ordenana           
r= 8000                      #radio que utilizaramos para la circuferencia          
dardos_totales =  1000000             #dardos totales a tirar
aumenta = 500000                      #dardos totales a aumentar por cada simulacio
maximo =  9000000                     #maximo de dardos a lanzar
ejex = []                             #datos a graficar en el eje x, es el total de dardos lanzados
ejey = []                             #datos a graficar en el eje y, son las aproximaciones de PI
dentro_a = []                         #se guarda la cantiada de dardos que calleron dentro en cada simulacion para mostrarlos en la tabala
pi = []                               #se guarda PI para poder mostrarlo como ocnstante en el grafico

#-------------------------------------codigo del dibujo------------------------
#red = pygame.Color("red")          
#cyan = pygame.Color("cyan")
#blue = pygame.Color(0,0,255)
#green = (0,255,0)
#white = (255,255,255)
#black = (0,0,0)
#pygame.init()
#screen = pygame.display.set_mode(((r*2),(r*2)))
#pygame.display.set_caption("calculo de pi")

#running= True
#screen.fill(black) 
#pygame.draw.circle(screen,white,(r,r),r)
#-------------------------------------------------------------------------------

while dardos_totales <=maximo:    #con este while 
  dentro = 0
  dardos = 0
  while dardos<= dardos_totales:  #con este while generamos los punto y calculamos donde callo
    #--------------codigo del dibujo----------------------
    #if dardos_totales==maximo:
      #for event in pygame.event.get():
       # if event.type==pygame.QUIT:
        #    running=False
    #-----------------------------------------------------
    x=random.randint(0, r*2)  #se genera la cordenada X
    y=random.randint(0, r*2)  #se genera la cordenada y
    dardos+=1                 #va aumentando en 1 la cantidad de dardos lanzados
    if math.sqrt(pow(x-r,2)+pow(y-r,2)) <= r: #con la ecucion de la circuferencia determinamos si callo dentro o fuera de la circuferencia 
      dentro+=1                               #se va contando cada vez que cae dentro
    #------------------codigo del dibujo-----------
      #if dardos_totales==maximo:
       # screen.set_at((x,y),red)
    #else:
      #if dardos_totales==maximo:
       # screen.set_at((x,y),blue)
    #----------------------------------------------
  dentro_a.append(dentro)                     #se guarda la cantidad de adrdos que calleron dentro para mostrarlos en la tabla
  ejex.append(dardos_totales)                 #se guarda la cantidad de dardos totale lanzados
  ejey.append((4*dentro)/(dardos_totales))    #se guarda la aproximacion de pi
  pi.append(3.1415)                           #se guarda el pi real para el grafico
  #------------------codigo del dibujo------------
  #if tdardos_totales==maximo:
    #pygame.display.flip()
  #-----------------------------------------------
  dardos_totales+=aumenta                     #se aumenta los dardos totales para la siguiente simulacion
#--------------------codigo del grafico----------------
plt.plot(ejex,ejey,marker="o",linestyle="-",color="r") 
plt.plot(ejex,pi,color="g")
plt.ylabel("PI")
plt.xlabel("Dardos lanzados")
plt.title("Aproximacion de PI segun los dardos")
plt.xticks(ejex)
plt.yticks([3.1350,3.1360,3.1370,3.1380,3.1390,3.140,3.1410,3.1415,3.1420,3.1430,3.1440,3.1450,3.1460,3.1470,3.1480,3.1490,3.1500])
plt.grid()
#--------------------------------------------------------
df= pd.DataFrame({"dardos":ejex,"dentro":dentro_a,"PI":ejey})#aqui creamos un dataframe para mostrar los datos de cada simulacion
print(df)                                                 #imprimimos la tabla
plt.show()                                                #mostramos el grafico
  