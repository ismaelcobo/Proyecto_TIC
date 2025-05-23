import random
import time

def jugar_ruleta():
    colores = {
        0: "verde",
        1: "rojo", 2: "negro", 3: "rojo", 4: "negro", 5: "rojo", 6: "negro",
        7: "rojo", 8: "negro", 9: "rojo", 10: "negro", 11: "negro", 12: "rojo",
        13: "negro", 14: "rojo", 15: "negro", 16: "rojo", 17: "negro", 18: "rojo",
        19: "rojo", 20: "negro", 21: "rojo", 22: "negro", 23: "rojo", 24: "negro",
        25: "rojo", 26: "negro", 27: "rojo", 28: "negro", 29: "negro", 30: "rojo",
        31: "negro", 32: "rojo", 33: "negro", 34: "rojo", 35: "negro", 36: "rojo"
    }

    resultados = {"rojo": 0, "negro": 0, "verde": 0}
    total_tiradas = 0

    print("🎰 Simulador de Ruleta - Ejecutando tiradas infinitas. Pulsa Ctrl+C para detenerlo.")
    try:
        while True:
            numero = random.randint(0, 36)
            color = colores[numero]
            resultados[color] += 1
            total_tiradas += 1

            if total_tiradas % 1000 == 0:
                print(f"Tiradas: {total_tiradas} | Rojo: {resultados['rojo']} | Negro: {resultados['negro']} | Verde: {resultados['verde']}")

    except KeyboardInterrupt:
        print("\n--- RESULTADOS FINALES ---")
        print(f"Tiradas totales: {total_tiradas}")
        print(f"Rojo: {resultados['rojo']} | Negro: {resultados['negro']} | Verde: {resultados['verde']}")
        print("Simulación finalizada.")

if __name__ == "__main__":
    jugar_ruleta()
