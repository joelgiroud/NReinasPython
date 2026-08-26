# ♕ Solucionador de N-Reinas: IA Multiparadigma (Python + Prolog)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Prolog](https://img.shields.io/badge/Prolog-E25A1C?style=for-the-badge)]()
[![Sockets](https://img.shields.io/badge/TCP/IP_Sockets-000000?style=for-the-badge)]()
[![Artificial Intelligence](https://img.shields.io/badge/AI_&_Logic-FF0000?style=for-the-badge)]()

##  Descripción del Proyecto
Este proyecto es una implementación de Inteligencia Artificial que resuelve el clásico problema de las **N-Reinas** utilizando una arquitectura de cliente-servidor multiparadigma. 

En lugar de utilizar un solo lenguaje, el sistema desacopla la lógica de inferencia matemática de la interfaz visual. Se emplea **Prolog** como motor de lógica pura (Backtracking y Satisfacción de Restricciones) y **Python** como orquestador y frontend gráfico, comunicando ambos procesos de manera síncrona a través de **Sockets TCP/IP**.

##  Arquitectura del Sistema

La solución está estructurada en tres capas principales que operan como procesos independientes:

* **Motor de Inferencia (Backend - Prolog):** 
  * `reinas.pl` y `SER.pl`: Contienen los algoritmos de búsqueda y las reglas lógicas. Prolog evalúa el árbol de decisiones, descartando ramas inválidas (pruning) mediante su motor de resolución nativo para encontrar las posiciones donde las reinas no se atacan entre sí.
* **Capa de Comunicación (Middleware - Sockets):** 
  * `Socket.py`: Establece un puente de red a bajo nivel (TCP/IP) permitiendo que Python envíe el tamaño del tablero y Prolog responda con las coordenadas calculadas, serializando y deserializando los datos en tiempo de ejecución.
* **Interfaz de Usuario (Frontend - Python):** 
  * `proyecto.py`: Consume los datos procesados por Prolog y renderiza dinámicamente el tablero de ajedrez, utilizando los assets gráficos (`reina.png`) para visualizar la solución final al usuario.

##  Conceptos Técnicos Demostrados
1. **Comunicación Inter-Procesos (IPC):** Dominio de conexiones por Sockets, manejo de puertos y flujos de red.
2. **Programación Lógica y Declarativa:** Aplicación de Inteligencia Artificial simbólica, manejando el problema de las N-Reinas como un CSP (*Constraint Satisfaction Problem*).
3. **Desacoplamiento de Sistemas:** Separación estricta entre la lógica de negocio (Prolog) y la capa de presentación (Python).

##  Cómo ejecutar este proyecto localmente

Para arrancar el sistema, es necesario ejecutar el servidor lógico y luego el cliente visual:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/joelgiroud/](https://github.com/joelgiroud/)[nombre-de-tu-repo].git

PD: Indispensable poder ejecutar este proyecto con Prolog y Python. Este software funciona con sockets.
