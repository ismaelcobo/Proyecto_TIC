# 🧪 Proyecto Comparativo: Rendimiento de VM vs Docker

Bienvenido al repositorio del proyecto de evaluación comparativa de rendimiento entre una máquina virtual (VM) y un contenedor Docker utilizando como caso de estudio un simulador de ruleta.

---

## 📝 Descripción del Proyecto

Este proyecto tiene como objetivo comparar el comportamiento de un mismo programa en dos entornos distintos:

* Una **máquina virtual** basada en VirtualBox  
* Un **contenedor Docker** en el sistema operativo host  

El programa utilizado es un simulador de ruleta (`ruleta_casino.py`) que ejecuta tiradas infinitas de forma continua. La comparación se ha realizado bajo condiciones controladas y equivalentes en ambos entornos, midiendo las siguientes métricas:

- **Consumo de CPU**
- **Uso de memoria RAM**
- **Espacio en disco ocupado**
- **Tiempo de arranque del programa**

---

## 📂 Estructura del Repositorio

```
PROYECTO_TIC/
└── Estructura_Proyecto/
└── vm_vs_docker_benchmark/
├── notebooks/
│ └── vm_vs_docker_comparison.ipynb
├── results/
│ ├── analisis_resultados.md
│ ├── capturaConsumoDocker.png
│ ├── capturaConsumoVM.png
│ ├── capturaEjecuciónDocker.png
│ ├── capturaEjecuciónVM.png
│ ├── grafico_comparativo_final.png
│ ├── tabla_comparativa_final.png
│ ├── capturaEspacioOcupadoVM.png
│ ├── capturaEspacioOcupadoDocker.png
│ ├── capturaTiempoEjecuciónVM.png
│ └── capturaTiempoEjecuciónDocker.png
├── scripts/
│ ├── Dockerfile
│ ├── docker_setup.sh
│ ├── ruleta_casino.py
│ ├── vm_setup.sh
│ └── arranque_test.py
├── .gitignore
├── install.ipynb
└── README.md
```

---


---

## ⚙️ Tecnologías Utilizadas

* **Python 3.10** (con librerías: `psutil`, `matplotlib`, `seaborn`)
* **VirtualBox** para entorno VM
* **Docker Desktop** para entorno contenedor
* **psrecord** para medir rendimiento en VM
* **docker stats** para medir rendimiento en Docker
* **comando `df -h /`** para espacio en disco en VM
* **`docker image ls`** para ver tamaño de imágenes en Docker
* **`time` y `Measure-Command`** para medir el tiempo de arranque

---

## 🚀 Instrucciones de Ejecución

1. Clonar el repositorio

2. En la **VM**:
   - Instalar dependencias:
     ```bash
     pip install psutil
     ```
   - Ejecutar el programa en segundo plano:
     ```bash
     nohup python3 ruleta_casino.py &
     ```
   - Medir el uso de recursos:
     ```bash
     psrecord <PID> --log stats_vm.txt --interval 1
     ```
   - Ver espacio en disco:
     ```bash
     df -h /
     ```
   - Medir tiempo de arranque:
     ```bash
     time (python3 ruleta_casino.py | head -n 1)
     ```

3. En **Docker**:
   - Construir la imagen:
     ```bash
     docker build -t ruleta-casino -f scripts/Dockerfile scripts
     ```
   - Ejecutar el contenedor:
     ```bash
     docker run -d --name ruleta-casino-cont ruleta-casino
     ```
   - Medir uso de recursos:
     ```bash
     docker stats ruleta-casino-cont --no-stream > results/stats_docker.txt
     ```
   - Ver espacio en disco ocupado:
     ```bash
     docker image ls
     ```
   - Medir tiempo de arranque:
     ```powershell
     Measure-Command { docker run --rm --entrypoint python3 ruleta-casino scripts/arranque_test.py }
     ```

---

## 📊 Resultados

Los resultados comparativos (CPU, RAM, disco y tiempo de arranque) se pueden consultar en:

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
