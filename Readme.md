# ♕ Solucionador de N-Reinas: IA Multiparadigma (Python + Prolog + Concurrencia)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Prolog](https://img.shields.io/badge/Prolog-E25A1C?style=for-the-badge)]()
[![Sockets](https://img.shields.io/badge/TCP/IP_Sockets-000000?style=for-the-badge)]()
[![Artificial Intelligence](https://img.shields.io/badge/AI_&_Logic-FF0000?style=for-the-badge)]()

##  Descripción del Proyecto
Este proyecto es una implementación de Inteligencia Artificial Clásica que resuelve el problema de las **N-Reinas** mediante una arquitectura distribuida y políglota de tipo Cliente-Servidor. 

El sistema desacopla la lógica de inferencia matemática de la interfaz visual. Se emplea **Prolog** como motor de lógica pura y concurrente (para resolución por *Backtracking* y satisfacción de restricciones) y **Python** como cliente para la orquestación y renderizado visual, comunicándose en tiempo real a través de **Sockets TCP/IP**.

##  Arquitectura del Sistema

La solución está estructurada en capas que operan como procesos y hilos independientes:

* **Backend Inteligente y Concurrente (Servidor Prolog - `SER.pl` & `reinas.pl`):**
  * Contiene los algoritmos de búsqueda y las reglas de negocio. Prolog evalúa el espacio de estados mediante su motor de resolución nativo para encontrar configuraciones válidas.
  * Implementa **hilos concurrentes (`thread_create`)** para atender múltiples peticiones de clientes de manera simultánea sin bloquear el canal principal de escucha.
* **Capa de Comunicación (Red / IPC):**
  * Manejo de Sockets TCP/IP a bajo nivel para la transmisión, serialización y recepción de datos estructurados entre procesos independientes.
* **Frontend / Cliente Visual (Python - `Socket.py` / `proyecto.py`):**
  * Establece la conexión de red, envía el parámetro del tablero al servidor, procesa la respuesta lógica y renderiza gráficamente la solución utilizando recursos visuales (`reina.png`).

##  Conceptos Técnicos Demostrados
1. **Concurrencia a Nivel de Servidor:** Manejo de hilos independientes en Prolog para gestión multiproceso de clientes.
2. **Comunicación Inter-Procesos (IPC):** Dominio de sockets de red TCP/IP, puertos y control de flujos de datos.
3. **Programación Lógica y Declarativa:** Inteligencia Artificial simbólica aplicada como un Problema de Satisfacción de Restricciones (CSP).
4. **Desacoplamiento de Sistemas:** Separación estricta entre el motor de inferencia analítica y la capa de presentación.

##  Cómo ejecutar este proyecto localmente

⚠️ **Requisito Indispensable:** Este software requiere tener instalado **SWI-Prolog** y **Python**. La comunicación depende estrictamente de sockets de red locales, por lo que se debe seguir un orden de ejecución preciso para evitar errores de conexión (*Connection Refused*).

### Paso 1: Iniciar el Servidor Lógico (Prolog)
Abre una terminal en la raíz del proyecto y levanta el servidor interactivo:
```bash
    swipl -s SER.pl
```
Una vez dentro de la consola de Prolog, inicializa el puerto de escucha ejecutando:
```bash
    ?- servidor.
```
### Paso 2: Ejecutar el Cliente (Python)
Abre una segunda terminal independiente y ejecuta el script del cliente para mandar la petición al servidor:
```bash
    python Socket.py
```

# Capturas de pantalla (screenshots)
![Ss_1](https://github.com/joelgiroud/NReinasPython/blob/main/Screenshots/SS1.png)
![Ss_2](https://github.com/joelgiroud/NReinasPython/blob/main/Screenshots/SS2.png)
