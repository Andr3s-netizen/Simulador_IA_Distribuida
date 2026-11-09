# 🤖 Simulador de Inteligencia Artificial Distribuida (Multi-Agente)

![Python](https://shields.io)
![License](https://shields.io)
![Build](https://shields.io)

Este proyecto es un aplicativo didáctico interactivo que implementa un **Sistema Multi-Agente (SMA)** para demostrar los conceptos fundamentales de la **Inteligencia Artificial Distribuida (IAD)** y la computación en el borde (*Edge Computing*).

A través de una interfaz gráfica sencilla, el sistema simula cómo una flota de robots autónomos puede coordinarse, negociar y tomar decisiones descentralizadas sin depender de un servidor inteligente central.

---

## 🚀 Características Clave

* **Inteligencia Local Decentralizada:** Cada robot actúa como un agente independiente con sensores propios (monitoreo de batería y posición geográfica).
* **Procesamiento Concurrente:** Simulación de hardware distribuido mediante subprocesos (`threading`) asíncronos en tiempo real.
* **Mecanismo de Consenso:** Implementación de un protocolo de subastas donde los agentes evalúan costos y eligen democráticamente al candidato óptimo.
* **Interfaz Gráfica Integrada:** Consola interactiva en Tkinter para visualizar la deliberación interna de los nodos de IA.

---

## 🛠️ Arquitectura de la IA Distribuida

El núcleo del aplicativo rompe con el paradigma de control centralizado basándose en tres principios:

1. **Evaluación de Heurística Local:** El sistema central publica la tarea, pero **no calcula las rutas de nadie**. Cada agente corre su propio algoritmo interno balanceando la distancia hacia el objetivo y su autonomía energética.
2. **Reglas Autónomas de Autoresguardo:** Si un agente detecta por medio de sus sensores que su batería es menor al 20%, su IA local toma de manera autónoma la decisión de rechazar la tarea para preservar el nodo.
3. **Resolución de Conflictos:** Los agentes interactúan de forma horizontal publicando sus ofertas en una "pizarra" común, resolviendo la asignación mediante un consenso de costo mínimo.

---

## 📦 Descarga e Instalación (Para Usuarios)

No necesitas tener Python instalado para probar esta simulación. Puedes ejecutar el aplicativo directamente en tu computadora siguiendo estos pasos:

1. Ve a la sección de **[Releases](enlace-a-tus-releases-aqui)** a la derecha de este repositorio.
2. Descarga el archivo ejecutable comprimido (ej. `ia_distribuida_gui.exe`).
3. Haz doble clic sobre el archivo descargado para iniciar el simulador de forma inmediata.

---

## 💻 Ejecución desde el Código Fuente (Desarrolladores)

Si prefieres auditar o modificar el código, asegúrate de contar con Python 3.9 o superior. Al usar librerías nativas del lenguaje (`tkinter`, `threading`), no requiere dependencias externas.

1. Clona este repositorio:
   ```bash
   git clone https://github.com
   ```
2. Entra al directorio del proyecto:
   ```bash
   cd TU_REPOSITORIO
   ```
3. Ejecuta el script principal:
   ```bash
   python ia_distribuida_gui.py
   ```

---

## 🏗️ Cómo se construyó el Ejecutable (`.exe`)

Para empaquetar este proyecto en un archivo independiente portable, se utilizó la herramienta `auto-py-to-exe`. Si deseas replicar el proceso, utiliza la siguiente configuración:

* **Script Path:** Selecciona tu archivo `ia_distribuida_gui.py`.
* **One File / One Directory:** Selecciona **One File** (para compilar todo en un único archivo ejecutable).
* **Console Window:** Selecciona **Window Based (hide the console)** (para que solo se muestre la interfaz gráfica estilizada del programa).

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo, modificarlo y distribuirlo para fines educativos.
