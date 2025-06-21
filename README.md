==============================================================
               SeloS DoS Toolkit v1.0 - by DozerMx
==============================================================

⚠️ USO LEGAL:
Este script está diseñado EXCLUSIVAMENTE con fines educativos y pruebas en entornos controlados.
NO LO UTILICES contra sistemas sin autorización expresa. Podrías incurrir en delitos informáticos.

----------------------------------------
🧠 DESCRIPCIÓN
----------------------------------------
SeloS es una herramienta de tráfico HTTP masivo construida con Python y aiohttp.
Usa tareas asíncronas para lanzar miles de requests GET con headers aleatorios, útil para:
- Pruebas de stress
- Análisis de capacidad de respuesta
- Verificación de WAFs

Incluye rotación de rutas, useragents y cabeceras para evadir detección básica.

----------------------------------------
💻 INSTALACIÓN EN LINUX
----------------------------------------

1. Actualiza el sistema:
   sudo apt update && sudo apt upgrade -y

2. Instala Python y pip:
   sudo apt install python3 python3-pip -y

3. (Opcional) Crea un entorno virtual:
   python3 -m venv venv
   source venv/bin/activate

4. Clona o descarga el script:
   git clone https://github.com/DozerMx/SeloS.git
   cd SeloS

5. Instala los requisitos:
   pip install -r requirements.txt

6. Ejecuta el script:
   python3 SeloS.py

----------------------------------------
📱 INSTALACIÓN EN TERMUX (Android)
----------------------------------------

1. Actualiza paquetes:
   pkg update && pkg upgrade -y

2. Instala Python y Git:
   pkg install python git -y

3. Clona el repositorio:
   git clone https://github.com/DozerMx/SeloS.git
   cd SeloS

4. Instala dependencias:
   pip install -r requirements.txt

5. Ejecuta el script:
   python SeloS.py

----------------------------------------
🧰 USO
----------------------------------------

Al ejecutar, te pedirá:

Target URL >> example.com
Workers (100-10000) >> 1500

- URL puede tener o no el http/https.
- Workers: número de tareas asíncronas (recomendado 500 a 2000 según tu CPU)

Se mostrará el código de estado HTTP de cada request para medir respuesta del servidor.

----------------------------------------
📦 REQUISITOS (requirements.txt)
----------------------------------------

aiohttp==3.9.5
pyfiglet==1.0.2

Python >= 3.8 (recomendado 3.11+)

----------------------------------------
📌 CONSEJOS TÉCNICOS
----------------------------------------

- Ideal para analizar carga y stress en tu servidor.
- No se recomienda usar más de 2000 workers si tu conexión o dispositivo es débil.
- Compatible con Termux, WSL, Linux y cualquier sistema con Python 3.

----------------------------------------
📩 AUTOR Y CONTACTO
------------------------------------------------------------

Autor: DozerMx
Versión: 1.0

¿Mejoras o sugerencias? Abre un issue o crea un pull request.

------------------------------------------------------------
🛡️ DISCLAIMER
------------------------------------------------------------

El uso de esta herramienta queda bajo TU responsabilidad.
El autor no se hace responsable del uso indebido o malicioso del código.
Usa esto con ética, inteligencia y respeto.

============================================================
