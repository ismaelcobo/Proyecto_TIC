import random

def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jugar():
    print("🎲 Bienvenido al Casino de Dados 🎲")
    puntuacion = 0

    while True:
        input("Pulsa ENTER para tirar los dados...")
        suma = tirar_dados()
        print(f"Has sacado un total de {suma}")
        puntuacion += suma
        print(f"Puntuación acumulada: {puntuacion}")

        if puntuacion >= 50:
            print("¡Ganaste! 🎉")
            break

if __name__ == "__main__":
    jugar()
