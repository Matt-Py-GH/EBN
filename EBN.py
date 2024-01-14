#A PRODUCTION BY: MMPROGRAMATIONCODE 2023 - 2024 PROCODEM
#THIS GAME WAS CREATED BY AN ALONE PROGRAMMER, WHO CREATED PROCODEM TOO. HIS COMPANY
#DEDICATED TO HER
#Por favor si usted encuentra este código, no lo difunda, úselo a modo recreativo, pero no lo comparta, me costó mucho hacerlo
#y probablemente me perjudicaría que se filtre, soy un programador novato, sepa disculpar mis errores.
#-----------------------------------------------------------------------------------------------------------------------------------

import pygame
import sys
import random
import os


pygame.init()
pygame.mixer.init()

#-----------------------------------------------------------------------------------------------------------------------------------
#Icono
icono = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\icon.ico")
pygame.display.set_icon(icono)

# Definir colores
menubg = (1, 8, 57)
white = (255, 255, 255)
botonbg = (52, 60, 111)
version = (32, 35, 55)
title = (69, 80, 153)
procodem = (64, 0 , 128)

#Sonidos
suspensotrack = pygame.mixer.Sound('C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\suspensotrack.mp3')
suspensotrack.play(-1)

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escape before night 1.11")
pygame.display.flip()
    
#Draws
fondo = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\fondo.png")
fondo = pygame.transform.scale(fondo, (450, 450))
pos_fondo = [200, 80]

empresa = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\procodem.png")
empresa = pygame.transform.scale(empresa, (800, 290))
pos_empresa = [0, 130]
#-----------------------------------------------------------------------------------------------------------------------------------

# Fuente y tamaño del texto
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 16)
font3 = pygame.font.Font(None, 40)

# Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y, color, font_size=36):
    font = pygame.font.Font(None, font_size)
    texto_superficie = font.render(texto, True, color)
    text_rect = texto_superficie.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(texto_superficie, text_rect)

# Función para crear botones
def crear_boton(x, y, ancho, alto, color, texto, accion=None):
    pygame.draw.rect(screen, color, (x, y, ancho, alto), 6)
    pygame.draw.rect(screen, white, (x, y, ancho, alto), 2)
    mostrar_texto(texto, x + 10, y + 10, white)
    rect_boton = pygame.Rect(x, y, ancho, alto)
    return rect_boton, accion

# Funciones para acciones de los botones
def iniciar_juego():
    global menu_activo
    suspensotrack.stop()
    menu_activo = False
        
def salir_juego():
    pygame.quit()
    sys.exit()
    
def pantalla_carga():
    progreso = 0
    ancho_carga = 520
    alto_carga = 20
    margen_horizontal = 130
    margen_vertical = 420
    fondo = pygame.Surface(screen.get_size())
    fondo.fill(procodem)
    margen_interior = 5
    
    while progreso < 100:
        pygame.time.delay(20)
        progreso += 1
        progreso_relativo = (progreso / 100) * (ancho_carga - 2 * margen_interior)
        screen.blit(fondo, (0, 0))
        screen.blit(empresa, pos_empresa)
        pygame.draw.rect(screen, (0, 0, 0), (margen_horizontal, margen_vertical, ancho_carga, alto_carga), 2)
        pygame.draw.rect(screen, white, (margen_horizontal + margen_interior, margen_vertical + margen_interior,
        progreso_relativo, alto_carga - 2 * margen_interior))
        pygame.display.update()

pantalla_carga()
        
menu_activo = True
while menu_activo:
    screen.fill(menubg)
    screen.blit(fondo, pos_fondo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if boton_iniciar.collidepoint((x, y)):
                iniciar_juego()
            elif boton_salir.collidepoint((x, y)):
                salir_juego()
    mostrar_texto("Escape before night", 275, 0, title, font_size=40)
    mostrar_texto("©MMProgramationCode 2024", 325, 585, version, font_size=16)
    mostrar_texto("Version 1.11", 0, 585, version, font_size=16)
    boton_iniciar, _ = crear_boton(0, 200, 100, 50, botonbg, "Start", iniciar_juego)
    boton_salir, _ = crear_boton(0, 400, 100, 50, botonbg, "Exit", salir_juego)    
    pygame.display.update()
#-----------------------------------------------------------------------------------------------------------------------------------

#Size
WIDTH, HEIGHT = 1420, 820

#Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Title
pygame.display.set_caption("Escape before night 1.11")

#Draws
pasto = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo.png"))
pasto = pygame.transform.scale(pasto, (WIDTH, HEIGHT))

pastodark1 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo2.png"))
pastodark1= pygame.transform.scale(pastodark1, (WIDTH, HEIGHT))

pastodark2 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo3.png"))
pastodark2= pygame.transform.scale(pastodark2, (WIDTH, HEIGHT))

pastodark3 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo4.png"))
pastodark3= pygame.transform.scale(pastodark3, (WIDTH, HEIGHT))

pastodark4 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo5.png"))
pastodark4= pygame.transform.scale(pastodark4, (WIDTH, HEIGHT))

pastodark5 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo6.png"))
pastodark5= pygame.transform.scale(pastodark5, (WIDTH, HEIGHT))

pastodark6 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo7.png"))
pastodark6= pygame.transform.scale(pastodark6, (WIDTH, HEIGHT))

pastodark7 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo8.png"))
pastodark7= pygame.transform.scale(pastodark7, (WIDTH, HEIGHT))

pastodark8 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo9.png"))
pastodark8= pygame.transform.scale(pastodark8, (WIDTH, HEIGHT))

pastodark9 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo10.png"))
pastodark9 = pygame.transform.scale(pastodark9, (WIDTH, HEIGHT))

pastodark10 = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\imagendefondo11.png"))
pastodark10= pygame.transform.scale(pastodark10, (WIDTH, HEIGHT))

noche = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\noche.png")
noche = pygame.transform.scale(noche, (WIDTH, HEIGHT))

imagen_game_over = pygame.image.load(os.path.join("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\jumpscare.png"))
imagen_game_over = pygame.transform.scale(imagen_game_over, (WIDTH, HEIGHT))

casucha = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\cabaña.png")
casucha = pygame.transform.scale(casucha, (300, 300))
pos_casucha = [-30, 0]

manzana = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\manzanoide.png")
manzana = pygame.transform.scale(manzana, (150, 150))
pos_manzanoide = [400, 100]

toky = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\toky.png")
toky = pygame.transform.scale(toky, (200, 200))
pos_toky = [700, 620]

bug = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\bug.png")
bug = pygame.transform.scale(bug, (220, 220))
pos_bug = [0, 200]

regadera = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\regadera.png")
regadera = pygame.transform.scale(regadera, (280, 280))
pos_regadera = [1200, 0]

instrucciones = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones.png")
instrucciones = pygame.transform.scale(instrucciones, (WIDTH, HEIGHT))

instrucciones2 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones2.png")
instrucciones2 = pygame.transform.scale(instrucciones2, (WIDTH, HEIGHT))

instrucciones3 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones3.png")
instrucciones3 = pygame.transform.scale(instrucciones3, (WIDTH, HEIGHT))

instrucciones4 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones4.png")
instrucciones4 = pygame.transform.scale(instrucciones4, (WIDTH, HEIGHT))

instrucciones5 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones5.png")
instrucciones5 = pygame.transform.scale(instrucciones5, (WIDTH, HEIGHT))

instrucciones6 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones6.png")
instrucciones6 = pygame.transform.scale(instrucciones6, (WIDTH, HEIGHT))

instrucciones7 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\instrucciones7.png")
instrucciones7 = pygame.transform.scale(instrucciones7, (WIDTH, HEIGHT))

bugui = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\bugui.png")
bugui = pygame.transform.scale(bugui, (220, 220))

bugui2 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\bugui.png")
bugui2 = pygame.transform.scale(bugui2, (220, 220))

bugui3 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\bugui.png")
bugui3 = pygame.transform.scale(bugui3, (220, 220))

bugui4 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\redbugui.png")
bugui4 = pygame.transform.scale(bugui4, (220, 220))

bugui5 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\MaxBugui.png")
bugui5 = pygame.transform.scale(bugui5, (220, 220))

youdied = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\youdied.png")
youdied = pygame.transform.scale(youdied, (WIDTH, HEIGHT))

win = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win.png")
win = pygame.transform.scale(win, (WIDTH, HEIGHT))

win2 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win2.png")
win2 = pygame.transform.scale(win2, (WIDTH, HEIGHT))

win3 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win3.png")
win3 = pygame.transform.scale(win3, (WIDTH, HEIGHT))

win4 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win4.png")
win4 = pygame.transform.scale(win4, (WIDTH, HEIGHT))

win5 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win5.png")
win5 = pygame.transform.scale(win5, (WIDTH, HEIGHT))

win6 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win6.png")
win6 = pygame.transform.scale(win6, (WIDTH, HEIGHT))

win7 = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\win7.png")
win7 = pygame.transform.scale(win7, (WIDTH, HEIGHT))

#Player
personaje_actual = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\derecha.png")
personaje_actual = pygame.transform.scale(personaje_actual, (320, 320))

personaje_derecha = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\derecha.png")
personaje_derecha = pygame.transform.scale(personaje_derecha, (320, 320))

personaje_izquierda = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\izquierda.png")
personaje_izquierda = pygame.transform.scale(personaje_izquierda, (320, 320))

personaje_espalda = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\espaldas.png")
personaje_espalda = pygame.transform.scale(personaje_espalda, (300, 300))

personaje_delante = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\delante.png")
personaje_delante = pygame.transform.scale(personaje_delante, (320, 300))

velocidad = 1
posicion_personaje = [-10, 140]

#Creditos
credits = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\credits.png")
credits = pygame.transform.scale(credits, (WIDTH, HEIGHT))

credofi = pygame.image.load("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\creditosoficiales.png")
credofi = pygame.transform.scale(credofi, (WIDTH, HEIGHT))

#Timers
tiempo_inicial_nivel_1 = pygame.time.get_ticks()
tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 200000

#Sonidos
sonido_game_over = pygame.mixer.Sound('C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\gameover.mp3')
soundtrack = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\soundtrackoriginal.mp3")
sonidorecogida = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\pickeo.mp3")
bugsound = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\bug.mp3")
winsound = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\winsound.mp3")
nextlevel = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\nextlevel.mp3")
finalsound = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\finalsound.mp3")
creditsound = pygame.mixer.Sound("C:\\Users\\mateo\\OneDrive\\Escritorio\\EBN\\creditsound.mp3")
#----------------------------------------------------------------------------------------------------------------------

#Variables previas del while
regadera_visible = True
toky_visible = True
manzana_visible = True
running = True
mostrar_pastodark1 = False
nivel1_completado = False
mostrar_bug = False
pd2 = False
pd3 = False
pd4 = False
pd5 = False
pd6 = False
pd7 = False
pd8 = False
pd9 = False
pd10 = False

#Bugui
rango_x_min = 680
rango_x_max = 700
rango_y_min = 610
rango_y_max = 620

pos_bugui = [random.randint(rango_x_min, rango_x_max), random.randint(rango_y_min, rango_y_max)]
velocidad_bug = 3

#Instrucciones y nivel
screen.blit(instrucciones, (0, 0))
nextlevel.play()
pygame.display.flip()
pygame.time.wait(5000)

vida = 30
soundtrack.play(-1)

#BUCLE DEL NIVEL 1 --------------------------------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)
                
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bugui[0] += movimiento_x * velocidad_bug
    pos_bugui[1] += movimiento_y * velocidad_bug
    pos_bugui[0] = max(rango_x_min, min(pos_bugui[0], rango_x_max))
    pos_bugui[1] = max(rango_y_min, min(pos_bugui[1], rango_y_max))

    pos_anterior = posicion_personaje.copy()
    
    if 15000 <= tiempo_transcurrido < 16000:
        mostrar_pastodark1 = True
        
    if 30000 <= tiempo_transcurrido < 31000:
        pd2 = True
        
    if 45000 <= tiempo_transcurrido < 46000:
        pd3 = True
    
    if 60000 <= tiempo_transcurrido < 61000:
        pd4 = True
        
    if 75000 <= tiempo_transcurrido < 76000:
        pd5 = True
        
    if 90000 <= tiempo_transcurrido < 91000:
        pd6 = True
        
    if 105000 <= tiempo_transcurrido < 106000:
        pd7 = True
    
    if 120000 == tiempo_transcurrido < 121000:
        pd8 = True
        
    if 135000 == tiempo_transcurrido< 136000:
        pd9 = True
    
    if 150000 <= tiempo_transcurrido < 151000:
        pd10 = True
        
    if 198000 <= tiempo_transcurrido < 200000:
        mostrar_bug = True
        bugsound.play()

    if tiempo_transcurrido >= 200000:
        screen.blit(imagen_game_over, (0, 0))
        bugsound.stop()
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False
        menu_activo = True

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
        
    #Dedicado a la manzana
    ancho_de_la_manzana = 30
    alto_de_la_manzana = 30
    hitbox_manzana = pygame.Rect(pos_manzanoide[0], pos_manzanoide[0], ancho_de_la_manzana, alto_de_la_manzana)
    hitbox_manzana.x = pos_manzanoide[0] + 55
    hitbox_manzana.y = pos_manzanoide[1] + 60
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    
    #Dedicado a la regadera
    anchoregadera = 50
    altoregadera = 50
    hitbox_regadera = pygame.Rect(pos_regadera[1], pos_regadera[1], anchoregadera, altoregadera)
    hitbox_regadera.x = pos_regadera[0] + 110
    hitbox_regadera.y = pos_regadera[1] + 110
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado a bugui
    anchobugui = 40
    altobugui = 40
    hitbox_bugui = pygame.Rect(pos_bugui[0], pos_bugui[1], anchobugui, altobugui)
    hitbox_bugui.x = pos_bugui[0] + 70
    hitbox_bugui.y = pos_bugui[1] + 90
    
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 0, 250), hitbox_regadera, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_manzana, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_casa, 1)
        pygame.display.flip()

    if hitbox_personaje.colliderect(hitbox_manzana) and manzana_visible:
            manzana_visible = False
            sonidorecogida.play()
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
            toky_visible = False
            sonidorecogida.play()
         
    if hitbox_personaje.colliderect(hitbox_regadera) and regadera_visible:
            regadera_visible = False
            sonidorecogida.play()
        
    if regadera_visible == False and manzana_visible == False and toky_visible == False and hitbox_personaje.colliderect(hitbox_casa): 
        screen.blit(win, (0, 0))
        soundtrack.stop()
        winsound.play()
        pygame.display.flip()
        pygame.time.wait(10000)
        nivel1_completado = True
        running = False
    
    if hitbox_personaje.colliderect(hitbox_bugui):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
        
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
        
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
           
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
           
    # Renderizado
    screen.blit(pasto, (0, 0))
    if mostrar_pastodark1:
        screen.blit(pastodark1, (0, 0))
    if pd2:
        screen.blit(pastodark2, (0, 0))
    if pd3:
        screen.blit(pastodark3, (0, 0))
    if pd4:
        screen.blit(pastodark4, (0, 0))
    if pd5:
        screen.blit(pastodark5, (0, 0))
    if pd6:
        screen.blit(pastodark6, (0, 0))
    if pd7:
        screen.blit(pastodark7, (0, 0))
    if pd8:
        screen.blit(pastodark8, (0, 0))
    if pd9:
        screen.blit(pastodark9, (0, 0))
    if pd10:
        screen.blit(pastodark10, (0, 0))
    if manzana_visible:
        screen.blit(manzana, pos_manzanoide)
    if toky_visible:
        screen.blit(toky, pos_toky)
    if regadera_visible:
        screen.blit(regadera, pos_regadera)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    screen.blit(bugui, pos_bugui)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)
    pygame.display.flip()
#FIN DEL NIVEL 1 ----------------------------------------------------------------------------------

#Variables previas del while
regadera_visible = True
toky_visible = True
manzana_visible = True
mostrar_pastodark1 = False
nivel2_completado = False
running2 = False
mostrar_bug = False
posicion_personaje = [-10, 140]
pd2 = False
pd3 = False
pd4 = False
pd5 = False
pd6 = False
pd7 = False
pd8 = False
pd9 = False
pd10 = False

tiempo_inicial_nivel_1 = pygame.time.get_ticks()
tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 170000

#Buguis
rango_x_min = 390
rango_x_max = 400
rango_y_min = 90
rango_y_max = 120

rango_x_min2 = 1180
rango_x_max2 = 1200
rango_y_min2 = 0
rango_y_max2 = 20


pos_bugui = [random.randint(rango_x_min2, rango_x_max2), random.randint(rango_y_min2, rango_y_max2)]
velocidad_bug2 = 3

pos_bugui2 = [random.randint(rango_x_min2, rango_x_max2), random.randint(rango_y_min2, rango_y_max2)]
velocidad_bug2 = 3

if nivel1_completado:
    vida = 30
    running2 = True
    tiempo_inicial_nivel_1 = pygame.time.get_ticks()
    tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 170000
    screen.blit(instrucciones2, (0, 0))
    nextlevel.play()
    pygame.display.flip()
    pygame.time.wait(5000)
    soundtrack.play(-1)
        
#BUCLE DEL NIVEL 2 --------------------------------------------------------------------------------
while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running2 = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)
                
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bugui[0] += movimiento_x * velocidad_bug
    pos_bugui[1] += movimiento_y * velocidad_bug
    pos_bugui[0] = max(rango_x_min, min(pos_bugui[0], rango_x_max))
    pos_bugui[1] = max(rango_y_min, min(pos_bugui[1], rango_y_max))
    
    pos_bugui2[0] += movimiento_x * velocidad_bug2
    pos_bugui2[1] += movimiento_y * velocidad_bug2
    pos_bugui2[0] = max(rango_x_min2, min(pos_bugui2[0], rango_x_max2))
    pos_bugui2[1] = max(rango_y_min2, min(pos_bugui2[1], rango_y_max2))
    
    pos_anterior = posicion_personaje.copy()
    
    if 15000 <= tiempo_transcurrido < 16000:
        mostrar_pastodark1 = True
        
    if 30000 <= tiempo_transcurrido < 31000:
        pd2 = True
        
    if 45000 <= tiempo_transcurrido < 46000:
        pd3 = True
    
    if 60000 <= tiempo_transcurrido < 61000:
        pd4 = True
        
    if 75000 <= tiempo_transcurrido < 76000:
        pd5 = True
        
    if 90000 <= tiempo_transcurrido < 91000:
        pd6 = True
        
    if 105000 <= tiempo_transcurrido < 106000:
        pd7 = True
    
    if 120000 == tiempo_transcurrido < 121000:
        pd8 = True
        
    if 135000 == tiempo_transcurrido< 136000:
        pd9 = True
    
    if 150000 <= tiempo_transcurrido < 151000:
        pd10 = True
        
    if 168000 <= tiempo_transcurrido < 170000:
        mostrar_bug = True

    if tiempo_transcurrido >= 170000:
        screen.blit(imagen_game_over, (0, 0))
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running2 = False

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
    
    #Dedicado a la manzana
    ancho_de_la_manzana = 30
    alto_de_la_manzana = 30
    hitbox_manzana = pygame.Rect(pos_manzanoide[0], pos_manzanoide[0], ancho_de_la_manzana, alto_de_la_manzana)
    hitbox_manzana.x = pos_manzanoide[0] + 55
    hitbox_manzana.y = pos_manzanoide[1] + 60
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    
    #Dedicado a la regadera
    anchoregadera = 50
    altoregadera = 50
    hitbox_regadera = pygame.Rect(pos_regadera[1], pos_regadera[1], anchoregadera, altoregadera)
    hitbox_regadera.x = pos_regadera[0] + 110
    hitbox_regadera.y = pos_regadera[1] + 110
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado a bugui
    anchobugui = 40
    altobugui= 40
    hitbox_bugui = pygame.Rect(pos_bugui[0], pos_bugui[1], anchobugui, altobugui)
    hitbox_bugui.x = pos_bugui[0] + 70
    hitbox_bugui.y = pos_bugui[1] + 90
    
    anchobugui2 = 40
    altobugui2= 40
    hitbox_bugui2 = pygame.Rect(pos_bugui2[0], pos_bugui2[1], anchobugui2, altobugui2)
    hitbox_bugui2.x = pos_bugui2[0] + 70
    hitbox_bugui2.y = pos_bugui2[1] + 90
    
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 0, 250), hitbox_regadera, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_manzana, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui2, 1)
        pygame.display.flip()

    if hitbox_personaje.colliderect(hitbox_manzana) and manzana_visible:
            manzana_visible = False
            sonidorecogida.play()
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
            toky_visible = False
            sonidorecogida.play()
         
    if hitbox_personaje.colliderect(hitbox_regadera) and regadera_visible:
            regadera_visible = False
            sonidorecogida.play()
            
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
        
    if regadera_visible == False and manzana_visible == False and toky_visible == False and hitbox_personaje.colliderect(hitbox_casa): 
        screen.blit(win2, (0, 0))
        soundtrack.stop()
        winsound.play()
        pygame.display.flip()
        pygame.time.wait(10000)
        nivel2_completado = True
        running2 = False
        
    if hitbox_personaje.colliderect(hitbox_bugui) or hitbox_personaje.colliderect(hitbox_bugui2):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
        
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
    
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
    
    # Renderizado
    screen.blit(pasto, (0, 0))
    if mostrar_pastodark1:
        screen.blit(pastodark1, (0, 0))
    if pd2:
        screen.blit(pastodark2, (0, 0))
    if pd3:
        screen.blit(pastodark3, (0, 0))
    if pd4:
        screen.blit(pastodark4, (0, 0))
    if pd5:
        screen.blit(pastodark5, (0, 0))
    if pd6:
        screen.blit(pastodark6, (0, 0))
    if pd7:
        screen.blit(pastodark7, (0, 0))
    if pd8:
        screen.blit(pastodark8, (0, 0))
    if pd9:
        screen.blit(pastodark9, (0, 0))
    if pd10:
        screen.blit(pastodark10, (0, 0))
    if manzana_visible:
        screen.blit(manzana, pos_manzanoide)
    if toky_visible:
        screen.blit(toky, pos_toky)
    if regadera_visible:
        screen.blit(regadera, pos_regadera)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    screen.blit(bugui, pos_bugui)
    screen.blit(bugui2, pos_bugui2)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)
    pygame.display.flip()
#FIN DEL NIVEL 2 ----------------------------------------------------------------------------------

#Variables previas del while
regadera_visible = True
toky_visible = True
manzana_visible = True
running3 = False
mostrar_pastodark1 = False
nivel3_completado = False
mostrar_bug = False
posicion_personaje = [-10, 140]
pd2 = False
pd3 = False
pd4 = False
pd5 = False
pd6 = False
pd7 = False
pd8 = False
pd9 = False
pd10 = False

#Buguis
rango_x_min = 690
rango_x_max = 700
rango_y_min = 610
rango_y_max = 620

rango_x_min2 = 1190
rango_x_max2 = 1200
rango_y_min2 = 0
rango_y_max2 = 20

rango_x_min3 = 380
rango_x_max3 = 400
rango_y_min3 = 90
rango_y_max3 = 120

pos_bugui = [random.randint(rango_x_min, rango_x_max), random.randint(rango_y_min, rango_y_max)]
velocidad_bug = 3

pos_bugui2 = [random.randint(rango_x_min2, rango_x_max2), random.randint(rango_y_min2, rango_y_max2)]
velocidad_bug2 = 3

pos_bugui3 = [random.randint(rango_x_min3, rango_x_max3), random.randint(rango_y_min3, rango_y_max3)]
velocidad_bug3 = 3
   
if nivel2_completado:
    running3 = True
    vida = 30
    tiempo_inicial_nivel_1 = pygame.time.get_ticks()
    tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 140000
    screen.blit(instrucciones3, (0, 0))
    nextlevel.play()
    pygame.display.flip()
    pygame.time.wait(5000)
    soundtrack.play(-1)
    
#BUCLE DEL NIVEL 3 --------------------------------------------------------------------------------
while running3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running3 = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running3 = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)  

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bugui[0] += movimiento_x * velocidad_bug
    pos_bugui[1] += movimiento_y * velocidad_bug
    pos_bugui[0] = max(rango_x_min, min(pos_bugui[0], rango_x_max))
    pos_bugui[1] = max(rango_y_min, min(pos_bugui[1], rango_y_max))
    
    pos_bugui2[0] += movimiento_x * velocidad_bug2
    pos_bugui2[1] += movimiento_y * velocidad_bug2
    pos_bugui2[0] = max(rango_x_min2, min(pos_bugui2[0], rango_x_max2))
    pos_bugui2[1] = max(rango_y_min2, min(pos_bugui2[1], rango_y_max2))
    
    pos_bugui3[0] += movimiento_x * velocidad_bug3
    pos_bugui3[1] += movimiento_y * velocidad_bug3
    pos_bugui3[0] = max(rango_x_min3, min(pos_bugui3[0], rango_x_max3))
    pos_bugui3[1] = max(rango_y_min3, min(pos_bugui3[1], rango_y_max3))
    
    pos_anterior = posicion_personaje.copy()
    
    if 15000 <= tiempo_transcurrido < 16000:
        mostrar_pastodark1 = True
        
    if 30000 <= tiempo_transcurrido < 31000:
        pd2 = True
        
    if 45000 <= tiempo_transcurrido < 46000:
        pd3 = True
    
    if 60000 <= tiempo_transcurrido < 61000:
        pd4 = True
        
    if 75000 <= tiempo_transcurrido < 76000:
        pd5 = True
        
    if 90000 <= tiempo_transcurrido < 91000:
        pd6 = True
        
    if 105000 <= tiempo_transcurrido < 106000:
        pd7 = True
    
    if 120000 == tiempo_transcurrido < 121000:
        pd8 = True
        
    if 130000 == tiempo_transcurrido< 131000:
        pd9 = True
    
    if 135000 <= tiempo_transcurrido < 136000:
        pd10 = True
        
    if 138000 <= tiempo_transcurrido < 140000:
        mostrar_bug = True

    if tiempo_transcurrido >= 140000:
        screen.blit(imagen_game_over, (0, 0))
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running3 = False

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
    
    #Dedicado a la manzana
    ancho_de_la_manzana = 30
    alto_de_la_manzana = 30
    hitbox_manzana = pygame.Rect(pos_manzanoide[0], pos_manzanoide[0], ancho_de_la_manzana, alto_de_la_manzana)
    hitbox_manzana.x = pos_manzanoide[0] + 55
    hitbox_manzana.y = pos_manzanoide[1] + 60
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    
    #Dedicado a la regadera
    anchoregadera = 50
    altoregadera = 50
    hitbox_regadera = pygame.Rect(pos_regadera[1], pos_regadera[1], anchoregadera, altoregadera)
    hitbox_regadera.x = pos_regadera[0] + 110
    hitbox_regadera.y = pos_regadera[1] + 110
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado a bugui
    anchobugui = 40
    altobugui= 40
    hitbox_bugui = pygame.Rect(pos_bugui[0], pos_bugui[1], anchobugui, altobugui)
    hitbox_bugui.x = pos_bugui[0] + 70
    hitbox_bugui.y = pos_bugui[1] + 90
    
    anchobugui2 = 40
    altobugui2= 40
    hitbox_bugui2 = pygame.Rect(pos_bugui2[0], pos_bugui2[1], anchobugui2, altobugui2)
    hitbox_bugui2.x = pos_bugui2[0] + 70
    hitbox_bugui2.y = pos_bugui2[1] + 90
    
    anchobugui3 = 40
    altobugui3 = 40
    hitbox_bugui3 = pygame.Rect(pos_bugui3[0], pos_bugui3[1], anchobugui3, altobugui3)
    hitbox_bugui3.x = pos_bugui3[0] + 70
    hitbox_bugui3.y = pos_bugui3[1] + 90
    
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 0, 250), hitbox_regadera, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_manzana, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui2, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui3, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_casa, 1)
        pygame.display.flip()

    if hitbox_personaje.colliderect(hitbox_manzana) and manzana_visible:
            manzana_visible = False
            sonidorecogida.play()
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
            toky_visible = False
            sonidorecogida.play()
         
    if hitbox_personaje.colliderect(hitbox_regadera) and regadera_visible:
            regadera_visible = False
            sonidorecogida.play()
            
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
        
    if regadera_visible == False and manzana_visible == False and toky_visible == False and hitbox_personaje.colliderect(hitbox_casa): 
        screen.blit(win3, (0, 0))
        soundtrack.stop()
        winsound.play()
        pygame.display.flip()
        pygame.time.wait(10000)
        nivel3_completado = True
        running3 = False
        
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
           
    if hitbox_personaje.colliderect(hitbox_bugui) or hitbox_personaje.colliderect(hitbox_bugui2) or hitbox_personaje.colliderect(hitbox_bugui3):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
            
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
    
    # Renderizado
    screen.blit(pasto, (0, 0))
    if mostrar_pastodark1:
        screen.blit(pastodark1, (0, 0))
    if pd2:
        screen.blit(pastodark2, (0, 0))
    if pd3:
        screen.blit(pastodark3, (0, 0))
    if pd4:
        screen.blit(pastodark4, (0, 0))
    if pd5:
        screen.blit(pastodark5, (0, 0))
    if pd6:
        screen.blit(pastodark6, (0, 0))
    if pd7:
        screen.blit(pastodark7, (0, 0))
    if pd8:
        screen.blit(pastodark8, (0, 0))
    if pd9:
        screen.blit(pastodark9, (0, 0))
    if pd10:
        screen.blit(pastodark10, (0, 0))
    if manzana_visible:
        screen.blit(manzana, pos_manzanoide)
    if toky_visible:
        screen.blit(toky, pos_toky)
    if regadera_visible:
        screen.blit(regadera, pos_regadera)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    screen.blit(bugui, pos_bugui)
    screen.blit(bugui2, pos_bugui2)
    screen.blit(bugui3, pos_bugui3)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)

    pygame.display.flip()
#FIN DEL NIVEL 3 ----------------------------------------------------------------------------------

#Variables previas del while
regadera_visible = True
toky_visible = True
manzana_visible = True
running4 = False
mostrar_pastodark1 = False
nivel4_completado = False
mostrar_bug = False
posicion_personaje = [-10, 140]
pd2 = False
pd3 = False
pd4 = False
pd5 = False
pd6 = False
pd7 = False
pd8 = False
pd9 = False
pd10 = False

#Buguis
rango_x_min = 690
rango_x_max = 700
rango_y_min = 610
rango_y_max = 620

rango_x_min2 = 1190
rango_x_max2 = 1200
rango_y_min2 = 0
rango_y_max2 = 20

rango_x_min3 = 630
rango_x_max3 = 630
rango_y_min3 = -30
rango_y_max3 = 700

rango_x_min4 = 370
rango_x_max4 = 410
rango_y_min4 = 70
rango_y_max4 = 120

pos_bugui = [random.randint(rango_x_min, rango_x_max), random.randint(rango_y_min, rango_y_max)]
velocidad_bug = 4

pos_bugui2 = [random.randint(rango_x_min2, rango_x_max2), random.randint(rango_y_min2, rango_y_max2)]
velocidad_bug2 = 4

pos_bugui3 = [random.randint(rango_x_min3, rango_x_max3), random.randint(rango_y_min3, rango_y_max3)]
velocidad_bug3 = 10

pos_bugui4 = [random.randint(rango_x_min4, rango_x_max4), random.randint(rango_y_min4, rango_y_max4)]
velocidad_bug4 = 8


if nivel3_completado:
    running4 = True
    vida = 30
    tiempo_inicial_nivel_1 = pygame.time.get_ticks()
    tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 110000
    screen.blit(instrucciones4, (0, 0))
    nextlevel.play()
    pygame.display.flip()
    pygame.time.wait(5000)
    soundtrack.play(-1)

#BUCLE DEL NIVEL 4 --------------------------------------------------------------------------------
while running4:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running4 = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running4 = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)
                
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bugui[0] += movimiento_x * velocidad_bug
    pos_bugui[1] += movimiento_y * velocidad_bug
    pos_bugui[0] = max(rango_x_min, min(pos_bugui[0], rango_x_max))
    pos_bugui[1] = max(rango_y_min, min(pos_bugui[1], rango_y_max))
    
    pos_bugui2[0] += movimiento_x * velocidad_bug2
    pos_bugui2[1] += movimiento_y * velocidad_bug2
    pos_bugui2[0] = max(rango_x_min2, min(pos_bugui2[0], rango_x_max2))
    pos_bugui2[1] = max(rango_y_min2, min(pos_bugui2[1], rango_y_max2))
    
    pos_bugui3[0] += movimiento_x * velocidad_bug3
    pos_bugui3[1] += movimiento_y * velocidad_bug3
    pos_bugui3[0] = max(rango_x_min3, min(pos_bugui3[0], rango_x_max3))
    pos_bugui3[1] = max(rango_y_min3, min(pos_bugui3[1], rango_y_max3))
    
    pos_bugui4[0] += movimiento_x * velocidad_bug4
    pos_bugui4[1] += movimiento_y * velocidad_bug4
    pos_bugui4[0] = max(rango_x_min4, min(pos_bugui4[0], rango_x_max4))
    pos_bugui4[1] = max(rango_y_min4, min(pos_bugui4[1], rango_y_max4))
    
    pos_anterior = posicion_personaje.copy()
    
    if 10000 <= tiempo_transcurrido < 11000:
        mostrar_pastodark1 = True
        
    if 24000 <= tiempo_transcurrido < 25000:
        pd2 = True
        
    if 45000 <= tiempo_transcurrido < 46000:
        pd3 = True
    
    if 60000 <= tiempo_transcurrido < 61000:
        pd4 = True
        
    if 75000 <= tiempo_transcurrido < 76000:
        pd5 = True
        
    if 80000 <= tiempo_transcurrido < 81000:
        pd6 = True
        
    if 85000 <= tiempo_transcurrido < 86000:
        pd7 = True
    
    if 90000 == tiempo_transcurrido < 91000:
        pd8 = True
        
    if 95000 == tiempo_transcurrido< 96000:
        pd9 = True
    
    if 100000 <= tiempo_transcurrido < 101000:
        pd10 = True
        
    if 109000 <= tiempo_transcurrido < 110000:
        mostrar_bug = True

    if tiempo_transcurrido >= 110000:
        screen.blit(imagen_game_over, (0, 0))
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running4 = False

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
    
    #Dedicado a la manzana
    ancho_de_la_manzana = 30
    alto_de_la_manzana = 30
    hitbox_manzana = pygame.Rect(pos_manzanoide[0], pos_manzanoide[0], ancho_de_la_manzana, alto_de_la_manzana)
    hitbox_manzana.x = pos_manzanoide[0] + 55
    hitbox_manzana.y = pos_manzanoide[1] + 60
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    
    #Dedicado a la regadera
    anchoregadera = 50
    altoregadera = 50
    hitbox_regadera = pygame.Rect(pos_regadera[1], pos_regadera[1], anchoregadera, altoregadera)
    hitbox_regadera.x = pos_regadera[0] + 110
    hitbox_regadera.y = pos_regadera[1] + 110
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado a bugui
    anchobugui = 40
    altobugui= 40
    hitbox_bugui = pygame.Rect(pos_bugui[0], pos_bugui[1], anchobugui, altobugui)
    hitbox_bugui.x = pos_bugui[0] + 70
    hitbox_bugui.y = pos_bugui[1] + 90
    
    anchobugui2 = 40
    altobugui2 = 40
    hitbox_bugui2 = pygame.Rect(pos_bugui2[0], pos_bugui2[1], anchobugui2, altobugui2)
    hitbox_bugui2.x = pos_bugui2[0] + 70
    hitbox_bugui2.y = pos_bugui2[1] + 90
    
    anchobugui3 = 40
    altobugui3 = 40
    hitbox_bugui3 = pygame.Rect(pos_bugui3[0], pos_bugui3[1], anchobugui3, altobugui3)
    hitbox_bugui3.x = pos_bugui3[0] + 70
    hitbox_bugui3.y = pos_bugui3[1] + 90
    
    anchobugui4 = 40
    altobugui4 = 40
    hitbox_bugui4 = pygame.Rect(pos_bugui4[0], pos_bugui4[1], anchobugui4, altobugui4)
    hitbox_bugui4.x = pos_bugui4[0] + 70
    hitbox_bugui4.y = pos_bugui4[1] + 90
    
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 0, 250), hitbox_regadera, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_manzana, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_casa, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui2, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui3, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui4, 1)
        pygame.display.flip()

    if hitbox_personaje.colliderect(hitbox_manzana) and manzana_visible:
            manzana_visible = False
            sonidorecogida.play()
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
            toky_visible = False
            sonidorecogida.play()
         
    if hitbox_personaje.colliderect(hitbox_regadera) and regadera_visible:
            regadera_visible = False
            sonidorecogida.play()
            
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
        
    if regadera_visible == False and manzana_visible == False and toky_visible == False and hitbox_personaje.colliderect(hitbox_casa): 
        screen.blit(win4, (0, 0))
        soundtrack.stop()
        winsound.play()
        pygame.display.flip()
        pygame.time.wait(10000)
        nivel4_completado = True
        running4 = False
        
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
           
    if hitbox_personaje.colliderect(hitbox_bugui) or hitbox_personaje.colliderect(hitbox_bugui2) or hitbox_personaje.colliderect(hitbox_bugui3) or hitbox_personaje.colliderect(hitbox_bugui4):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
    
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
    
    # Renderizado
    screen.blit(pasto, (0, 0))
    if mostrar_pastodark1:
        screen.blit(pastodark1, (0, 0))
    if pd2:
        screen.blit(pastodark2, (0, 0))
    if pd3:
        screen.blit(pastodark3, (0, 0))
    if pd4:
        screen.blit(pastodark4, (0, 0))
    if pd5:
        screen.blit(pastodark5, (0, 0))
    if pd6:
        screen.blit(pastodark6, (0, 0))
    if pd7:
        screen.blit(pastodark7, (0, 0))
    if pd8:
        screen.blit(pastodark8, (0, 0))
    if pd9:
        screen.blit(pastodark9, (0, 0))
    if pd10:
        screen.blit(pastodark10, (0, 0))
    if manzana_visible:
        screen.blit(manzana, pos_manzanoide)
    if toky_visible:
        screen.blit(toky, pos_toky)
    if regadera_visible:
        screen.blit(regadera, pos_regadera)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    screen.blit(bugui, pos_bugui)
    screen.blit(bugui2, pos_bugui2)
    screen.blit(bugui3, pos_bugui3)
    screen.blit(bugui4, pos_bugui4)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)
    pygame.display.flip()
#FIN DEL NIVEL 4 ----------------------------------------------------------------------------------

#Variables previas del while
regadera_visible = True
toky_visible = True
manzana_visible = True
running5 = False
mostrar_pastodark1 = False
nivel5_completado = False
mostrar_bug = False
posicion_personaje = [-10, 140]
pd2 = False
pd3 = False
pd4 = False
pd5 = False
pd6 = False
pd7 = False
pd8 = False
pd9 = False
pd10 = False

#Buguis
rango_x_min2 = 1190
rango_x_max2 = 1200
rango_y_min2 = 0
rango_y_max2 = 20

rango_x_min3 = 630
rango_x_max3 = 630
rango_y_min3 = -30
rango_y_max3 = 700

rango_x_min4 = 370
rango_x_max4 = 410
rango_y_min4 = 70
rango_y_max4 = 120

rango_x_min5 = 690
rango_x_max5 = 730
rango_y_min5 = 610
rango_y_max5 = 650

pos_bugui2 = [random.randint(rango_x_min2, rango_x_max2), random.randint(rango_y_min2, rango_y_max2)]
velocidad_bug2 = 5

pos_bugui3 = [random.randint(rango_x_min3, rango_x_max3), random.randint(rango_y_min3, rango_y_max3)]
velocidad_bug3 = 5

pos_bugui4 = [random.randint(rango_x_min4, rango_x_max4), random.randint(rango_y_min4, rango_y_max4)]
velocidad_bug4 = 7

pos_bugui5 = [random.randint(rango_x_min5, rango_x_max5), random.randint(rango_y_min5, rango_y_max5)]
velocidad_bug5 = 9

if nivel4_completado:
    running5 = True
    vida = 30
    tiempo_inicial_nivel_1 = pygame.time.get_ticks()
    tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 80000
    screen.blit(instrucciones5, (0, 0))
    nextlevel.play()
    pygame.display.flip()
    pygame.time.wait(5000)
    soundtrack.play(-1)
    
#BUCLE DEL NIVEL 5 --------------------------------------------------------------------------------
while running5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running5 = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running5 = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)       

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bugui2[0] += movimiento_x * velocidad_bug2
    pos_bugui2[1] += movimiento_y * velocidad_bug2
    pos_bugui2[0] = max(rango_x_min2, min(pos_bugui2[0], rango_x_max2))
    pos_bugui2[1] = max(rango_y_min2, min(pos_bugui2[1], rango_y_max2))
    
    pos_bugui3[0] += movimiento_x * velocidad_bug3
    pos_bugui3[1] += movimiento_y * velocidad_bug3
    pos_bugui3[0] = max(rango_x_min3, min(pos_bugui3[0], rango_x_max3))
    pos_bugui3[1] = max(rango_y_min3, min(pos_bugui3[1], rango_y_max3))
    
    pos_bugui4[0] += movimiento_x * velocidad_bug4
    pos_bugui4[1] += movimiento_y * velocidad_bug4
    pos_bugui4[0] = max(rango_x_min4, min(pos_bugui4[0], rango_x_max4))
    pos_bugui4[1] = max(rango_y_min4, min(pos_bugui4[1], rango_y_max4))
    
    pos_bugui5[0] += movimiento_x * velocidad_bug5
    pos_bugui5[1] += movimiento_y * velocidad_bug5
    pos_bugui5[0] = max(rango_x_min5, min(pos_bugui5[0], rango_x_max5))
    pos_bugui5[1] = max(rango_y_min5, min(pos_bugui5[1], rango_y_max5))
    
    pos_anterior = posicion_personaje.copy()
    
    if 15000 <= tiempo_transcurrido < 16000:
        mostrar_pastodark1 = True
        
    if 30000 <= tiempo_transcurrido < 31000:
        pd2 = True
        
    if 35000 <= tiempo_transcurrido < 36000:
        pd3 = True
    
    if 40000 <= tiempo_transcurrido < 41000:
        pd4 = True
        
    if 45000 <= tiempo_transcurrido < 46000:
        pd5 = True
        
    if 50000 <= tiempo_transcurrido < 51000:
        pd6 = True
        
    if 65000 <= tiempo_transcurrido < 66000:
        pd7 = True
    
    if 70000 == tiempo_transcurrido < 71000:
        pd8 = True
        
    if 75000 == tiempo_transcurrido< 76000:
        pd9 = True
    
    if 77000 <= tiempo_transcurrido < 78000:
        pd10 = True
        
    if 79000 <= tiempo_transcurrido < 80000:
        mostrar_bug = True

    if tiempo_transcurrido >= 80000:
        screen.blit(imagen_game_over, (0, 0))
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running5 = False

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
    
    #Dedicado a la manzana
    ancho_de_la_manzana = 30
    alto_de_la_manzana = 30
    hitbox_manzana = pygame.Rect(pos_manzanoide[0], pos_manzanoide[0], ancho_de_la_manzana, alto_de_la_manzana)
    hitbox_manzana.x = pos_manzanoide[0] + 55
    hitbox_manzana.y = pos_manzanoide[1] + 60
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    
    #Dedicado a la regadera
    anchoregadera = 50
    altoregadera = 50
    hitbox_regadera = pygame.Rect(pos_regadera[1], pos_regadera[1], anchoregadera, altoregadera)
    hitbox_regadera.x = pos_regadera[0] + 110
    hitbox_regadera.y = pos_regadera[1] + 110
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado a bugui
    anchobugui2 = 40
    altobugui2 = 40
    hitbox_bugui2 = pygame.Rect(pos_bugui2[0], pos_bugui2[1], anchobugui2, altobugui2)
    hitbox_bugui2.x = pos_bugui2[0] + 70
    hitbox_bugui2.y = pos_bugui2[1] + 90
    
    anchobugui3 = 40
    altobugui3 = 40
    hitbox_bugui3 = pygame.Rect(pos_bugui3[0], pos_bugui3[1], anchobugui3, altobugui3)
    hitbox_bugui3.x = pos_bugui3[0] + 70
    hitbox_bugui3.y = pos_bugui3[1] + 90
    
    anchobugui4 = 40
    altobugui4 = 40
    hitbox_bugui4 = pygame.Rect(pos_bugui4[0], pos_bugui4[1], anchobugui4, altobugui4)
    hitbox_bugui4.x = pos_bugui4[0] + 70
    hitbox_bugui4.y = pos_bugui4[1] + 90
    
    anchobugui5 = 40
    altobugui5 = 40
    hitbox_bugui5 = pygame.Rect(pos_bugui5[0], pos_bugui5[1], anchobugui5, altobugui5)
    hitbox_bugui5.x = pos_bugui5[0] + 70
    hitbox_bugui5.y = pos_bugui5[1] + 90
    
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 0, 250), hitbox_regadera, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_manzana, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_casa, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui2, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui3, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui4, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui5, 1)
        pygame.display.flip()

    if hitbox_personaje.colliderect(hitbox_manzana) and manzana_visible:
            manzana_visible = False
            sonidorecogida.play()
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
            toky_visible = False
            sonidorecogida.play()
         
    if hitbox_personaje.colliderect(hitbox_regadera) and regadera_visible:
            regadera_visible = False
            sonidorecogida.play()
            
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
        
    if regadera_visible == False and manzana_visible == False and toky_visible == False and hitbox_personaje.colliderect(hitbox_casa): 
        screen.blit(win5, (0, 0))
        soundtrack.stop()
        winsound.play()
        pygame.display.flip()
        pygame.time.wait(10000)
        nivel5_completado = True
        running5 = False
        
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
           
    if hitbox_personaje.colliderect(hitbox_bugui2) or hitbox_personaje.colliderect(hitbox_bugui3) or hitbox_personaje.colliderect(hitbox_bugui4) or hitbox_personaje.colliderect(hitbox_bugui5):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
      
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
    
    # Renderizado
    screen.blit(pasto, (0, 0))
    if mostrar_pastodark1:
        screen.blit(pastodark1, (0, 0))
    if pd2:
        screen.blit(pastodark2, (0, 0))
    if pd3:
        screen.blit(pastodark3, (0, 0))
    if pd4:
        screen.blit(pastodark4, (0, 0))
    if pd5:
        screen.blit(pastodark5, (0, 0))
    if pd6:
        screen.blit(pastodark6, (0, 0))
    if pd7:
        screen.blit(pastodark7, (0, 0))
    if pd8:
        screen.blit(pastodark8, (0, 0))
    if pd9:
        screen.blit(pastodark9, (0, 0))
    if pd10:
        screen.blit(pastodark10, (0, 0))
    if manzana_visible:
        screen.blit(manzana, pos_manzanoide)
    if toky_visible:
        screen.blit(toky, pos_toky)
    if regadera_visible:
        screen.blit(regadera, pos_regadera)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    screen.blit(bugui2, pos_bugui2)
    screen.blit(bugui3, pos_bugui3)
    screen.blit(bugui4, pos_bugui4)
    screen.blit(bugui5, pos_bugui5)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)
    pygame.display.flip()
#FIN DEL NIVEL 5 ----------------------------------------------------------------------------------

#Variables previas del while
regadera_visible = True
toky_visible = True
manzana_visible = True
running6 = False
mostrar_pastodark1 = False
nivel6_completado = False
mostrar_bug = False
posicion_personaje = [-10, 140]
pd2 = False
pd3 = False
pd4 = False
pd5 = False
pd6 = False
pd7 = False
pd8 = False
pd9 = False
pd10 = False

#Buguis
rango_x_min2 = 1170
rango_x_max2 = 1200
rango_y_min2 = 0
rango_y_max2 = 30

rango_x_min3 = 630
rango_x_max3 = 630
rango_y_min3 = -30
rango_y_max3 = 700

rango_x_min4 = 360
rango_x_max4 = 410
rango_y_min4 = 70
rango_y_max4 = 130

rango_x_min5 = 690
rango_x_max5 = 730
rango_y_min5 = 610
rango_y_max5 = 650

pos_bugui2 = [random.randint(rango_x_min2, rango_x_max2), random.randint(rango_y_min2, rango_y_max2)]
velocidad_bug2 = 7

pos_bugui3 = [random.randint(rango_x_min3, rango_x_max3), random.randint(rango_y_min3, rango_y_max3)]
velocidad_bug3 = 7

pos_bugui4 = [random.randint(rango_x_min4, rango_x_max4), random.randint(rango_y_min4, rango_y_max4)]
velocidad_bug4 = 10

pos_bugui5 = [random.randint(rango_x_min5, rango_x_max5), random.randint(rango_y_min5, rango_y_max5)]
velocidad_bug5 = 10

if nivel5_completado:
    running6 = True
    vida = 30
    tiempo_inicial_nivel_1 = pygame.time.get_ticks()
    tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 50000
    screen.blit(instrucciones6, (0, 0))
    nextlevel.play()
    pygame.display.flip()
    pygame.time.wait(5000)
    soundtrack.play(-1)
    
#BUCLE DEL NIVEL 6 --------------------------------------------------------------------------------
while running6:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running6 = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running6 = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)
                
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bugui2[0] += movimiento_x * velocidad_bug2
    pos_bugui2[1] += movimiento_y * velocidad_bug2
    pos_bugui2[0] = max(rango_x_min2, min(pos_bugui2[0], rango_x_max2))
    pos_bugui2[1] = max(rango_y_min2, min(pos_bugui2[1], rango_y_max2))
    
    pos_bugui3[0] += movimiento_x * velocidad_bug3
    pos_bugui3[1] += movimiento_y * velocidad_bug3
    pos_bugui3[0] = max(rango_x_min3, min(pos_bugui3[0], rango_x_max3))
    pos_bugui3[1] = max(rango_y_min3, min(pos_bugui3[1], rango_y_max3))
    
    pos_bugui4[0] += movimiento_x * velocidad_bug4
    pos_bugui4[1] += movimiento_y * velocidad_bug4
    pos_bugui4[0] = max(rango_x_min4, min(pos_bugui4[0], rango_x_max4))
    pos_bugui4[1] = max(rango_y_min4, min(pos_bugui4[1], rango_y_max4))
    
    pos_bugui5[0] += movimiento_x * velocidad_bug5
    pos_bugui5[1] += movimiento_y * velocidad_bug5
    pos_bugui5[0] = max(rango_x_min5, min(pos_bugui5[0], rango_x_max5))
    pos_bugui5[1] = max(rango_y_min5, min(pos_bugui5[1], rango_y_max5))
    
    pos_anterior = posicion_personaje.copy()
    
    if 15000 <= tiempo_transcurrido < 16000:
        mostrar_pastodark1 = True
        
    if 17000 <= tiempo_transcurrido < 18000:
        pd2 = True
        
    if 21000 <= tiempo_transcurrido < 22000:
        pd3 = True
    
    if 25000 <= tiempo_transcurrido < 26000:
        pd4 = True
        
    if 33000 <= tiempo_transcurrido < 34000:
        pd5 = True
        
    if 38000 <= tiempo_transcurrido < 39000:
        pd6 = True
        
    if 42000 <= tiempo_transcurrido < 43000:
        pd7 = True
    
    if 44000 == tiempo_transcurrido < 45000:
        pd8 = True
        
    if 46000 == tiempo_transcurrido< 47000:
        pd9 = True
    
    if 48000 <= tiempo_transcurrido < 49000:
        pd10 = True
        
    if 49000 <= tiempo_transcurrido < 49200:
        mostrar_bug = True

    if tiempo_transcurrido >= 50000:
        screen.blit(imagen_game_over, (0, 0))
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running6 = False

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
    
    #Dedicado a la manzana
    ancho_de_la_manzana = 30
    alto_de_la_manzana = 30
    hitbox_manzana = pygame.Rect(pos_manzanoide[0], pos_manzanoide[0], ancho_de_la_manzana, alto_de_la_manzana)
    hitbox_manzana.x = pos_manzanoide[0] + 55
    hitbox_manzana.y = pos_manzanoide[1] + 60
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    
    #Dedicado a la regadera
    anchoregadera = 50
    altoregadera = 50
    hitbox_regadera = pygame.Rect(pos_regadera[1], pos_regadera[1], anchoregadera, altoregadera)
    hitbox_regadera.x = pos_regadera[0] + 110
    hitbox_regadera.y = pos_regadera[1] + 110
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado a bugui
    anchobugui2 = 40
    altobugui2 = 40
    hitbox_bugui2 = pygame.Rect(pos_bugui2[0], pos_bugui2[1], anchobugui2, altobugui2)
    hitbox_bugui2.x = pos_bugui2[0] + 70
    hitbox_bugui2.y = pos_bugui2[1] + 90
    
    anchobugui3 = 40
    altobugui3 = 40
    hitbox_bugui3 = pygame.Rect(pos_bugui3[0], pos_bugui3[1], anchobugui3, altobugui3)
    hitbox_bugui3.x = pos_bugui3[0] + 70
    hitbox_bugui3.y = pos_bugui3[1] + 90
    
    anchobugui4 = 40
    altobugui4 = 40
    hitbox_bugui4 = pygame.Rect(pos_bugui4[0], pos_bugui4[1], anchobugui4, altobugui4)
    hitbox_bugui4.x = pos_bugui4[0] + 70
    hitbox_bugui4.y = pos_bugui4[1] + 90
    
    anchobugui5 = 40
    altobugui5 = 40
    hitbox_bugui5 = pygame.Rect(pos_bugui5[0], pos_bugui5[1], anchobugui5, altobugui5)
    hitbox_bugui5.x = pos_bugui5[0] + 70
    hitbox_bugui5.y = pos_bugui5[1] + 90
    
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 0, 250), hitbox_regadera, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_manzana, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui2, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui3, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui4, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bugui5, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_casa, 1)
        pygame.display.flip()

    if hitbox_personaje.colliderect(hitbox_manzana) and manzana_visible:
            manzana_visible = False
            sonidorecogida.play()
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
            toky_visible = False
            sonidorecogida.play()
            
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
         
    if hitbox_personaje.colliderect(hitbox_regadera) and regadera_visible:
            regadera_visible = False
            sonidorecogida.play()
        
    if regadera_visible == False and manzana_visible == False and toky_visible == False and hitbox_personaje.colliderect(hitbox_casa): 
        screen.blit(win6, (0, 0))
        soundtrack.stop()
        winsound.play()
        pygame.display.flip()
        pygame.time.wait(10000)
        nivel6_completado = True
        running6 = False
        
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
           
    if hitbox_personaje.colliderect(hitbox_bugui2) or hitbox_personaje.colliderect(hitbox_bugui3) or hitbox_personaje.colliderect(hitbox_bugui4) or hitbox_personaje.colliderect(hitbox_bugui5):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
    
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
    
    # Renderizado
    screen.blit(pasto, (0, 0))
    if mostrar_pastodark1:
        screen.blit(pastodark1, (0, 0))
    if pd2:
        screen.blit(pastodark2, (0, 0))
    if pd3:
        screen.blit(pastodark3, (0, 0))
    if pd4:
        screen.blit(pastodark4, (0, 0))
    if pd5:
        screen.blit(pastodark5, (0, 0))
    if pd6:
        screen.blit(pastodark6, (0, 0))
    if pd7:
        screen.blit(pastodark7, (0, 0))
    if pd8:
        screen.blit(pastodark8, (0, 0))
    if pd9:
        screen.blit(pastodark9, (0, 0))
    if pd10:
        screen.blit(pastodark10, (0, 0))
    if manzana_visible:
        screen.blit(manzana, pos_manzanoide)
    if toky_visible:
        screen.blit(toky, pos_toky)
    if regadera_visible:
        screen.blit(regadera, pos_regadera)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    screen.blit(bugui2, pos_bugui2)
    screen.blit(bugui3, pos_bugui3)
    screen.blit(bugui4, pos_bugui4)
    screen.blit(bugui5, pos_bugui5)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)
    pygame.display.flip()
#FIN DEL NIVEL 6 ----------------------------------------------------------------------------------

#Variables previas del while
toky_visible = True
running7 = False
mostrar_pastodark1 = False
nivel7_completado = False
mostrar_bug = False
posicion_personaje = [-10, 140]

#Final boss
rango_x_min = 0
rango_x_max = 1200
rango_y_min = 0
rango_y_max = 800

pos_bug = [1100, 10]
velocidad_bug = 0
    
if nivel6_completado:
    running7 = True
    vida = 20
    velocidad = 3
    tiempo_inicial_nivel_1 = pygame.time.get_ticks()
    tiempo_final_nivel_1 = tiempo_inicial_nivel_1 + 30000
    screen.blit(instrucciones7, (0, 0))
    nextlevel.play()
    pygame.display.flip()
    pygame.time.wait(5000)  
    soundtrack.play(-1)
    
#BUCLE DEL NIVEL 7 --------------------------------------------------------------------------------
while running7:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running7 = False
        if event.type == pygame.USEREVENT and 'reduce_life' in event.dict and event.dict['reduce_life']:
            vida -= 1
            if vida <= 0:
                soundtrack.stop()
                sonido_game_over.play()
                running7 = False
                screen.blit(youdied, (0, 0))
                pygame.display.flip()
                pygame.time.wait(5000)
                
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial_nivel_1
    
    movimiento_x = random.randint(-1, 1)
    movimiento_y = random.randint(-1, 1)
    
    pos_bug[0] += movimiento_x * velocidad_bug
    pos_bug[1] += movimiento_y * velocidad_bug
    pos_bug[0] = max(rango_x_min, min(pos_bug[0], rango_x_max))
    pos_bug[1] = max(rango_y_min, min(pos_bug[1], rango_y_max))
    
    pos_anterior = posicion_personaje.copy()

    if tiempo_transcurrido >= 30000:
        screen.blit(imagen_game_over, (0, 0))
        sonido_game_over.play()
        pygame.display.flip()
        pygame.time.wait(5000)
        running7 = False

    # Lógica de movimiento del personaje
    keys = pygame.key.get_pressed()
    pos_anterior = posicion_personaje.copy()

    if keys[pygame.K_w]:
        posicion_personaje[1] -= velocidad
        personaje_actual = personaje_espalda
    if keys[pygame.K_s]:
        posicion_personaje[1] += velocidad
        personaje_actual = personaje_delante
    if keys[pygame.K_a]:
        posicion_personaje[0] -= velocidad
        personaje_actual = personaje_izquierda
    if keys[pygame.K_d]:
        personaje_actual = personaje_derecha
        posicion_personaje[0] += velocidad
    
    #Dedicado a la casa
    ancho_de_la_casa = 200
    alto_de_la_casa = 190
    hitbox_casa = pygame.Rect(pos_casucha[0], pos_casucha[0], ancho_de_la_casa, alto_de_la_casa)
    hitbox_casa.x = pos_casucha[0] + 55
    hitbox_casa.y = pos_casucha[1] + 60
    
    #Dedicado al Toky
    anchotoky = 40
    altotoky= 40
    hitbox_toky = pygame.Rect(pos_toky[1], pos_toky[1], anchotoky, altotoky)
    hitbox_toky.x = pos_toky[0] + 80
    hitbox_toky.y = pos_toky[1] + 80
    pos_toky = [1200, 400]
    
    #Dedicado al personaje
    anchopersonaje = 30
    altopersonaje= 50
    hitbox_personaje = pygame.Rect(posicion_personaje[0], posicion_personaje[1], anchopersonaje, altopersonaje)
    hitbox_personaje.x += 125
    hitbox_personaje.y += 130
    
    #Dedicado al final boss
    anchobug = 90
    altobug = 110
    hitbox_bug = pygame.Rect(pos_bug[0], pos_bug[1], anchobug, altobug)
    hitbox_bug.x = pos_bug[0] + 70
    hitbox_bug.y = pos_bug[1] + 90
        
    if hitbox_personaje.colliderect(hitbox_toky) and toky_visible:
        random.randint(rango_x_min, rango_x_max), random.randint(rango_y_min, rango_y_max)
        toky_visible = False
        mostrar_bug = True
        velocidad_bug = 50
            
    if keys[pygame.K_e] and keys[pygame.K_b] and keys[pygame.K_n]:
        pygame.draw.rect(screen, (255, 100, 0), hitbox_toky, 1)
        pygame.draw.rect(screen, (255, 255, 255), hitbox_personaje, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitbox_bug, 1)
        pygame.display.flip()
            
    if hitbox_personaje.colliderect(hitbox_casa):
        posicion_personaje = pos_anterior
        
    if hitbox_personaje.colliderect(hitbox_bug):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'reduce_life': True}))
        
    if toky_visible == False and hitbox_personaje.colliderect(hitbox_casa):
        running7 = False
        nivel7_completado = True
        screen.blit(win7, (0, 0))
        soundtrack.stop()
        finalsound.play()
        pygame.display.flip()
        pygame.time.wait(7000)
        finalsound.stop()
        creditsound.play()
        screen.blit(credits, (0, 0))
        pygame.display.flip()
        pygame.time.wait(4500)
        screen.blit(credofi, (0, 0))
        pygame.display.flip()
        pygame.time.wait(4500)
    
    if hitbox_personaje.colliderect(pygame.Rect(0, 0, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, HEIGHT - 10, WIDTH, 10)) or \
       hitbox_personaje.colliderect(pygame.Rect(0, 0, 10, HEIGHT)) or \
       hitbox_personaje.colliderect(pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)):
           posicion_personaje = pos_anterior
    
    ancho_barra_vida = 10
    alto_barra_vida = 20
    color_barra_llena = (255, 0, 0)
    color_barra_vacia = (0, 0, 0)
    
    # Renderizado
    screen.blit(noche, (0, 0))
    if toky_visible:
        screen.blit(toky, pos_toky)
    screen.blit(casucha, pos_casucha)
    if mostrar_bug:
        screen.blit(bug, pos_bug)
    screen.blit(personaje_actual, posicion_personaje)
    ancho_vida = (vida / 3) * ancho_barra_vida
    pos_x = 1200
    pos_y = 10
    barra_vida_llena = pygame.Rect(pos_x, pos_y, ancho_vida, alto_barra_vida)
    barra_vida_vacia = pygame.Rect(pos_x + ancho_vida, pos_y, ancho_barra_vida - ancho_vida, alto_barra_vida)
    pygame.draw.rect(screen, color_barra_llena, barra_vida_llena)
    pygame.draw.rect(screen, color_barra_vacia, barra_vida_vacia)
    pygame.display.flip()
#FIN DEL NIVEL 7 ----------------------------------------------------------------------------------
