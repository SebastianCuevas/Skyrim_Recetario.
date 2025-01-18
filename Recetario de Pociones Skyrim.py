import time

print("""██████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████▒▓█████░▓████████████████████████████████████████
████████████████████████████████████████▒▒▓█████▓░▓███████████████████████████████████████
███████████████████████████████████████▒░██▓█████▓░▓██████████████████████████████████████
██████████████████████████████████████▒░▒██▓▒▓▓███░░▓█████████████████████████████████████
█████████████████████████████████████▒░░███░░░▒▒██▓░░█████████████████████████████████████
████████████████████████████████████▓░░▒██▓▓███▓░██░░░████████████████████████████████████
███████████████████████████████████▓░░░▒█████▓▓▒▓█▓░░░░███████████████████████████████████
██████████████████████████████████▓░░░▒█▓██▒░▓████▓█░░░░██████████████████████████████████
█████████████████████████████████▓░░░░████▓░░███████▓░░░░█████████████████████████████████
█████████████████████████████████░░░░▒██▓▒▒░░░░▓▒▒███░░░░▒████████████████████████████████
█████████████████████████████████▒░░░░░░░░░░░░░░░░░░░░░░░▓████████████████████████████████
██████████████████████████████████▒░░░░░░░░░░░░░░░░░░░░░▓█████████████████████████████████
███████████████████████████████████▒░░░░▒░░░░░░░░░▒░░░░▓██████████████████████████████████
████████████████████████████████████░░░▒████▒░░▓▓██░░░▓███████████████████████████████████
█████████████████████████████████████░░▓█████░░▓███▒░▒████████████████████████████████████
██████████████████████████████████████░░▒████▒░▓█▓▒░▒█████████████████████████████████████
███████████████████████████████████████░░░███░▒██░░░██████████████████████████████████████
████████████████████████████████████████░░██░▓███░░███████████████████████████████████████
████████████████████████████████████████▓░██░████░████████████████████████████████████████
█████████████████████████████████████████▓██▒█████████████████████████████████████████████
███████████████████████████████████████████░▓█████████████████████████████████████████████
███████████████████████████████████████████▓░▓▒▓██████████████████████████████████████████
████████████████████████████████████████████▓░▒███████████████████████████████████████████
█████████████████████████████████████████████▓████████████████████████████████████████████""")
time.sleep(2)
print("")
print("")

print("""Básicas:

1. Poción de curación.
2. Poción de aguante.
3. Poción de magia.
4. Poción de curar enfermedad.

Especiales:

5. Poción de invisibilidad.
6. Poción de respiración acuática.
7. Poción de fuerza.

Fortalecer:

8. Poción del herrero.
9. Poción del encantador.
10. Poción de berserk.
11. Poción del guerrero.
12. Poción de disparo certero.
13. Poción del caballero.
14. Poción del escaramuzador.

15. Poción de destrucción.
16. Poción de restauración.
17. Poción del conjurador.
18. Poción de alteración.
19. Poción de ilusión.

Venenos:

20. Veneno de parálisis.
21. Veneno de daño a la salud.

22. Finalizar programa.""")

while True:
    try:
        print("")
        print("Escribe un número:")
        print("")
        respuesta = float(input())

        if respuesta == 1:
            print("Ingredientes: Ala de dardo azul, ala de mariposa, corazón de daedra, flor azul de montaña, heces de diablillo, huevo de acantiza minero, jalea de saltador de cenizas (DB), ojo de gato sable, piel chamuscada de skeever, plumas de golondrina marina de Felsaad (DB), ranúnculo encorvado, trigo, vaina fúngica del pantano.")
        elif respuesta == 2:
            print("Ingredientes: Garras de oso, Abeja, Piel chamuscada de skeever, Ojo de gato sable, Pico de halcón, Carpa de hist, Panal, Cornamenta grande, Quitina de cangrejo del barro, Ala de dardo naranja, Perla, Huevo de zorzal, Colmillo de mamut molido, Flor púrpura de montaña, Diente de gato sable, Perca de lomo plateado, Perla pequeña, Tórax de luciérnaga, Jalea de netch (DB).")
        elif respuesta == 3:
            print("Ingredientes: Corazón de espino, Raíz trepadora, Aceite enano, Ectoplasma, Oreja de elfo, Sales de fuego, Sales de escarcha, Liquen gigante, Carne humana, Azúcar lunar, Mora Tapinella, Perla, Flor roja de montaña, Raíz nudosa, Polvo de vampiro.")
        elif respuesta == 4:
            print("Ingredientes: Piel chamuscada de skeever, Quitina de cangrejo del barro, Polvo de vampiro, Pluma de halcón, Plumas de golondrina marina de Felsaad (DG).")
        elif respuesta == 5:
            print("Ingredientes: Ala de actias luna, Dientes de espectro del hielo, Huevos de cauro, Polvo de vampiro, Raíz de nirn carmesí, Raíz de nirn, Raíz trepadora cenicienta (DB).")
        elif respuesta == 6:
            print("Ingredientes: Carpa de hist, Huevas de salmón (HF), Huevo de gallina, Huevo de halcón (HF), Percebe nórdico.")
        elif respuesta == 7:
            print("Ingredientes: Dedo del gigante, Pico de halcón, Betty de río, Foliota escamosa, Enseres de fuego fatuo, Raíz trepadora.")
        elif respuesta == 8:
            print("Ingredientes: Seta brillante, Diente de gato sable, Ranúnculo encorvado, Savia de spriggan.")
        elif respuesta == 9:
            print("Ingredientes: Ala de mariposa azul, Garra de bruja cuervo, Sinforicarpos, Savia de spriggan, Ala de polilla ancestral (DG), Antena de cauro cazador (DG), Ceniza de engendro (DB).")
        elif respuesta == 10:
            print("Ingredientes: Lengua de dragón, Amanita muscaria, Grasa de trol, Musgo de parasol de emperador (DB).")
        elif respuesta == 11:
            print("Ingredientes: Garras de oso, Raíz canina, Musgo colgante, Pluma de halcón, Huevo de acantiza minero, Perla pequeña.")
        elif respuesta == 12:
            print("Ingredientes: Raíz canina, Oreja de elfo, Frutos de enebro, Huevo de araña.")
        elif respuesta == 13:
            print("Ingredientes: Escamas de pez abisal, Diente de gato sable, Dientes de espectro del hielo, Rama de cardo, Sombrero blanco.")
        elif respuesta == 14:
            print("Ingredientes: Cola de skeever, Envoltorio de colmena, Pluma de halcón, Panal, Ala de actias luna, Jalea de saltador de cenizas (DB), Plumas de golondrina marina de Felsaad (DB).")
        elif respuesta == 15:
            print("Ingredientes: Aleta larga abacea, Cola de espada cyrodílica, Cornamenta pequeña, Flor amarilla de montaña DG, Montón de sal, Perla pequeña.")
        elif respuesta == 16:
            print("Ingredientes: Envoltorio de colmena, Ectoplasma, Polvo brillante, Seta brillante, Belladama, Enseres de fuego fatuo, Raíz trepadora cenicienta (DB).")
        elif respuesta == 17:
            print("Ingredientes: Cenizas de Berit, Ala de mariposa azul, Flor azul de montaña, Polvo de huesos, Antena de cazador de chaurus, Sales de escarcha, Plumas de hagraven, Lavanda.")
        elif respuesta == 18:
            print("Ingredientes: Polvo de huesos, Cenizas de Berit, Flor azul de montaña, Ala de mariposa azul, Lavanda, Plumas de bruja cuervo, Sales de escarcha, Ala de polilla ancestral (DG), Antena de cauro cazador (DG).")
        elif respuesta == 19:
            print("Ingredientes: Lengua de dragón, Aceite enano, Mora Tapinella, Raíz nudosa, Foliota escamosa.")
        elif respuesta == 20:
            print("Ingredientes: Corazón de espino, Raíz canina, Carne humana, Heces de diablillo, Vaina fúngica del pantano, Brote resplandeciente DG, Jalea de netch (DB).")
        elif respuesta == 21:
            print("Ingredientes: Raíz de nirn carmesí, Campanilla de la muerte, Ectoplasma, Oreja de falmer, Carne humana, Corazón humano, Heces de diablillo, Raíz de Jarrin, Belladama, Raíz de Nirn, Betty de río, Cola de Skeever, Cornamenta pequeña, Grasa de trol, Sales de vacío.")
        elif respuesta == 22:
            print("Programa finalizado.")
            break
        else:
            print("Error: Ese número no está disponible.")
    except ValueError:
        print("Error: Solo se admiten numeros. Intenta de nuevo.")









