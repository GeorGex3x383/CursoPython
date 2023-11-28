import pygame

# Inicializa a pygame
pygame.init()

# Creamos la pantalla de interfaz
pantalla = pygame.display.set_mode((800,600))

#Título e ícono
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("ovni-volando.png")
pygame.display.set_icon(icono)

#Variables del Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

def jugador(x,y):
    #Funcion que arroja en pantalla al jugador
    pantalla.blit(img_jugador,(x,y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    #Se pinta la pantalla primero 
    pantalla.fill((29,200,211))
    
    #Iterrar eventos
    for evento in pygame.event.get():
        #Evento de cerrar la pestaña
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #Evento de presionar una tecla de flecha (izquierda o derceha)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
                
        #Evento de soltar una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Actualizar la posicion de acuerdo a la tecla presionada
    jugador_x += jugador_x_cambio
    
    #Mantener jugador dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    #Se llama para pintar al jugador
    jugador(jugador_x,jugador_y)
    
    #Actualiza la pantalla
    pygame.display.update()