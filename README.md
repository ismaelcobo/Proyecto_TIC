# 🧪 Proyecto Comparativo: Rendimiento de VM vs Docker

Bienvenido al repositorio del proyecto de evaluación comparativa de rendimiento entre una máquina virtual (VM) y un contenedor Docker utilizando como caso de estudio un simulador de ruleta.

---

## 📝 Descripción del Proyecto

Este proyecto tiene como objetivo comparar el consumo de recursos (CPU y RAM) al ejecutar el mismo programa en dos entornos distintos:

* Una **máquina virtual** basada en VirtualBox
* Un **contenedor Docker** en el sistema operativo host

El programa utilizado es un simulador de ruleta (`ruleta_casino.py`) que ejecuta tiradas infinitas de forma continua. La comparación se ha realizado bajo condiciones controladas y equivalentes en ambos entornos.

---

## 📂 Estructura del Repositorio

```
PROYECTO_TIC/
└── Estructura_Proyecto/
    └── vm_vs_docker_benchmark/
        ├── notebooks/
        │   └── vm_vs_docker_comparison.ipynb
        ├── results/
        │   ├── analisis_resultados.md
        │   ├── capturaDatosDocker.png
        │   ├── capturaDatosVM.png
        │   ├── capturaEjecuciónDocker.png
        │   ├── capturaEjecuciónVM.png
        │   ├── grafico_comparativo.png
        │   └── tabla_comparativa.png
        ├── scripts/
        │   ├── Dockerfile
        │   ├── docker_setup.sh
        │   ├── ruleta_casino.py
        │   └── vm_setup.sh
        ├── .gitignore
        ├── install.ipynb
        └── README.md
```

---

## ⚙️ Tecnologías Utilizadas

* **Python 3.10** (con librerías: `psutil`, `matplotlib`, `seaborn`)
* **VirtualBox** para entorno VM
* **Docker Desktop** para entorno contenedor
* **psrecord** para medir rendimiento en VM
* **docker stats** para medir rendimiento en Docker

---

## 🚀 Instrucciones de Ejecución

### En la VM (Ubuntu Server):

1. Clonar el repositorio
2. Instalar dependencias:

   ```bash
   pip install psutil
   ```
3. Ejecutar el programa en segundo plano:

   ```bash
   nohup python3 ruleta_casino.py &
   ```
4. Medir con:

   ```bash
   psrecord <PID> --log stats_vm.txt --interval 1
   ```

### En Docker:

1. Construir la imagen:

   ```bash
   docker build -t ruleta-casino -f scripts/Dockerfile scripts
   ```
2. Ejecutar el contenedor:

   ```bash
   docker run -d --name ruleta-casino-cont ruleta-casino
   ```
3. Medir con:

   ```bash
   docker stats ruleta-casino-cont --no-stream > results/stats_docker.txt
   ```

---

## 📊 Resultados

Los resultados comparativos (CPU y RAM) se pueden consultar en:

🔎 [`results/analisis_resultados.md`](results/analisis_resultados.md)

Incluye:

* Capturas originales de mediciones
* Tabla de comparación
* Gráfico visual
* Conclusión final sobre el rendimiento

---

## 📬 Autor

**Ismael Cobo**
Proyecto desarrollado en el marco de la asignatura de TIC
Grado en Ingeniería Informática
Universidad Europea del Atlántico
