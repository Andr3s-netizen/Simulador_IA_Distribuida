import tkinter as tk
from tkinter import messagebox
import threading
import time
import random

# --- CLASE DE IA DISTRIBUIDA (AGENTE) ---
class RobotAgente:
    def __init__(self, nombre, ubicacion_inicial, bateria_inicial):
        self.nombre = nombre
        self.ubicacion = ubicacion_inicial  # Coordenada del 1 al 10
        self.bateria = bateria_inicial      # 0% a 100%
        self.oferta_actual = None

    def evaluar_tarea(self, ubicacion_tarea, log_callback):
        """Cada agente calcula autónomamente su propio costo."""
        distancia = abs(self.ubicacion - ubicacion_tarea)
        
        if self.bateria < 20:
            self.oferta_actual = float('inf')
            log_callback(f"❌ [{self.nombre}] Rechaza la tarea. Batería baja ({self.bateria}%).\n")
        else:
            # Algoritmo local: balance entre cercanía y batería restante
            self.oferta_actual = distancia + (100 - self.bateria) / 10
            log_callback(f"🤖 [{self.nombre}] Evaluando... Distancia: {distancia}, Batería: {self.bateria}%. Costo local: {self.oferta_actual:.2f}\n")

    def ejecutar_tarea(self, ubicacion_tarea, log_callback):
        """El agente realiza la tarea de forma autónoma."""
        log_callback(f"🚀 ¡{self.nombre} gana la subasta! Moviéndose a la ubicación {ubicacion_tarea}...\n")
        time.sleep(1.5)  # Simula el tiempo de desplazamiento
        self.ubicacion = ubicacion_tarea
        self.bateria -= random.randint(10, 18)  # Gasta energía
        if self.bateria < 0: self.bateria = 0
        log_callback(f"✅ [{self.nombre}] ¡Tarea completada! Nueva ubicación: {self.ubicacion}, Batería: {self.bateria}%\n\n")


# --- CLASE DE LA INTERFAZ GRÁFICA (GUI) ---
class AplicativoIA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de IA Distribuida - Multiagente")
        self.geometry("550x500")
        self.configure(bg="#f0f2f5")

        # Inicializamos los 3 agentes autónomos
        self.robots = [
            RobotAgente("Robot-Alfa", ubicacion_inicial=2, bateria_inicial=90),
            RobotAgente("Robot-Beta", ubicacion_inicial=8, bateria_inicial=85),
            RobotAgente("Robot-Omega", ubicacion_inicial=5, bateria_inicial=15) # Iniciará bajo de batería
        ]

        self.crear_componentes()
        self.actualizar_estado_robots()

    def crear_componentes(self):
        # Título principal
        lbl_titulo = tk.Label(self, text="Sistema de Subasta Distribuida", font=("Arial", 14, "bold"), bg="#f0f2f5", fg="#333")
        lbl_titulo.pack(pady=10)

        # Panel de Estado de los Robots
        self.frame_robots = tk.LabelFrame(self, text=" Estado Actual de los Agentes (Sensores) ", font=("Arial", 10, "bold"), bg="#f0f2f5", padx=10, pady=5)
        self.frame_robots.pack(fill="x", padx=15, pady=5)
        
        self.lbl_estados = tk.Label(self.frame_robots, text="", font=("Courier", 10), justify="left", bg="#f0f2f5")
        self.lbl_estados.pack(anchor="w")

        # Control de nueva tarea
        frame_control = tk.Frame(self, bg="#f0f2f5")
        frame_control.pack(pady=10)

        tk.Label(frame_control, text="Ubicación de Nueva Tarea (1 al 10):", font=("Arial", 10), bg="#f0f2f5").grid(row=0, column=0, padx=5)
        self.entry_tarea = tk.Entry(frame_control, width=8, font=("Arial", 10), justify="center")
        self.entry_tarea.grid(row=0, column=1, padx=5)
        self.entry_tarea.insert(0, "6") # Valor por defecto

        self.btn_enviar = tk.Button(frame_control, text="Asignar Tarea", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.procesar_subasta_hilo)
        self.btn_enviar.grid(row=0, column=2, padx=10)

        # Consola de logs de comunicación distribuidos
        lbl_logs = tk.Label(self, text="Consola de Comunicación entre Agentes:", font=("Arial", 10, "bold"), bg="#f0f2f5")
        lbl_logs.pack(anchor="w", padx=15)

        self.txt_logs = tk.Text(self, height=14, font=("Courier", 9), bg="#1e1e1e", fg="#ffffff", padx=10, pady=10)
        self.txt_logs.pack(fill="both", expand=True, padx=15, pady=5)

    def actualizar_estado_robots(self):
        """Muestra en la interfaz los datos de los sensores de cada robot."""
        texto = ""
        for r in self.robots:
            texto += f"🤖 {r.nombre:<11} -> Posición: {r.ubicacion:<2} | Batería: {r.bateria:>3}%\n"
        self.lbl_estados.config(text=texto)

    def log(self, mensaje):
        """Escribe las decisiones distribuidas en la consola negra de la interfaz."""
        self.txt_logs.insert(tk.END, mensaje)
        self.txt_logs.see(tk.END)

    def procesar_subasta_hilo(self):
        """Lanza el proceso en un hilo separado para que la interfaz gráfica no se congele."""
        try:
            ub_tarea = int(self.entry_tarea.get())
            if not (1 <= ub_tarea <= 10): raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número entero válido entre 1 y 10.")
            return

        self.btn_enviar.config(state="disabled")
        # El proceso de IA distribuida corre en paralelo
        threading.Thread(target=self.ejecutar_sistema_distribuido, args=(ub_tarea,), daemon=True).start()

    def ejecutar_sistema_distribuido(self, ubicacion_tarea):
        self.log(f"📢 [SISTEMA] Nueva tarea publicada en ubicación: {ubicacion_tarea}\n")
        self.log("--------------------------------------------------\n")
        
        # 1. Ejecución Distribuida: Cada agente calcula su oferta simultáneamente
        hilos_agentes = []
        for robot in self.robots:
            hilo = threading.Thread(target=robot.evaluar_tarea, args=(ubicacion_tarea, self.log))
            hilos_agentes.append(hilo)
            hilo.start()

        for hilo in hilos_agentes:
            hilo.join()

        # 2. Mecanismo de Consenso: Se evalúa quién ofreció el menor costo
        ganador = min(self.robots, key=lambda r: r.oferta_actual)

        if ganador.oferta_actual == float('inf'):
            self.log("❌ [SISTEMA] Subasta cancelada: Ningún agente tiene condiciones óptimas.\n\n")
        else:
            # El agente ganador realiza la tarea de forma autónoma
            ganador.ejecutar_tarea(ubicacion_tarea, self.log)
            self.actualizar_estado_robots()

        self.log("--------------------------------------------------\n")
        self.btn_enviar.config(state="normal")


if __name__ == "__main__":
    app = AplicativoIA()
    app.mainloop()
