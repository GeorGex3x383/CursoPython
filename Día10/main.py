import pygame
import random
import math
from pygame import mixer

# Inicializa a pygame
pygame.init()

# Creamos la pantalla de interfaz
pantalla = pygame.display.set_mode((800,600))

#Título, ícono y fondo
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("ovni-volando.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")

#Agregar música
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#Variables del Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

def jugador(x,y):
    #Funcion que arroja en pantalla al jugador
    pantalla.blit(img_jugador,(x,y))

#Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("alien-pixelado.png"))
    enemigo_y.append(random.randint(50,200))
    enemigo_x.append(random.randint(0, 736))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

def enemigo(x,y,ene):
    #Funcion que arroja en pantalla al enemigo
    pantalla.blit(img_enemigo[ene],(x,y))
    
#Variables de la bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

def disparar_bala(x,y):
    #Funcion disparar la bala
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))
    
# Colisión
def hay_colision(x_1,y_1,x_2,y_2):
    #Función para detectar colisión
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2-y_1,2))
    if distancia < 13.5:
        return True
    else:
        return False
    
# Puntuación
puntuacion = 0
fuente = pygame.font.Font('Transcorner.ttf',20)
texto_x = 10
texto_y = 10

def mostrar_puntuacion(x,y):
    #Función para mostrar puntuación en pantalla
    texto = fuente.render(f"Puntuacion: {puntuacion}",True, (0,0,0))
    pantalla.blit(texto,(x,y))
    
#Texto final del juego
fuente_final = pygame.font.Font('Transcorner.ttf',60)

def texto_final():
    #Función para mostrar en pantalla fin del juego
    mi_fuente_final = fuente_final.render("Game Over",True,(0,0,0))
    pantalla.blit(mi_fuente_final,(200,200))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    #Se pinta imagen de fondo
    pantalla.blit(fondo,(0,0))
    
    #Iterrar eventos
    for evento in pygame.event.get():
        #Evento de cerrar la pestaña
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #Evento de presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                nueva_bala = {
                "x": jugador_x,
                "y": jugador_y,
                "velocidad": -1
                }
            balas.append(nueva_bala)
                
        #Evento de soltar una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Actualizar la posicion del jugador de acuerdo a la tecla presionada
    jugador_x += jugador_x_cambio
    
    #Mantener jugador dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    #Actualizar la posicion del enemigo
    for e in range(cantidad_enemigos):
        
        #Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        
        enemigo_x[e] += enemigo_x_cambio[e]
    
    #Mantener enemigo dentro de bordes y dar movimiento izq/der y hacia abajo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
    
    #Verificar colisión
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntuacion += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)
        
    #Se llama para pintar al enemigo
        enemigo(enemigo_x[e],enemigo_y[e],e)
        
    #Movimiento de la bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
        
    #Se llama para pintar al jugador
    jugador(jugador_x,jugador_y)
    
    #Se llama para pintar la puntuación
    mostrar_puntuacion(texto_x,texto_y)
    
    #Actualiza la pantalla
    pygame.display.update()