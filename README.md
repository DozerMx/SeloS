================
                 🚀 SeloS DoS Toolkit v1.0 - by DozerMx
================

![Python](https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/status-educational-lightgrey?style=flat-square)

> Herramienta educativa para DoS
tráfico HTTP masivo de forma asíncrona.

------------------------------------------------------------
📋 Tabla de Contenido
------------------------------------------------------------

1. Descripción
2. Requisitos
3. Instalación
    - Linux
    - Termux
4. Uso
5. Funcionamiento Interno
6. Capturas
7. Advertencia Legal
8. Autor
9. Disclaimer

------------------------------------------------------------
📌 DESCRIPCIÓN
------------------------------------------------------------

SeloS DoS Toolkit es un script Python para pruebas de stress HTTP, que envía peticiones masivas asíncronas usando aiohttp. Simula tráfico realista y variado con rotación de headers y rutas, ideal para pruebas de carga, pentesting local o análisis de WAFs.

------------------------------------------------------------
🧰 REQUISITOS
------------------------------------------------------------

- Python 3.8 o superior (recomendado 3.11+)
- pip
- Librerías:
    - aiohttp==3.9.5
    - pyfiglet==1.0.2

Archivo requirements.txt:

aiohttp==3.9.5  
pyfiglet==1.0.2

------------------------------------------------------------
⚙️ INSTALACIÓN
------------------------------------------------------------

🐧 LINUX

1. Instalar dependencias:

sudo apt update && sudo apt install python3 python3-pip git -y

2. Clonar el repositorio:

git clone https://github.com/DozerMx/SeloS.git  
cd SeloS

3. Instalar requisitos:

pip install -r requirements.txt

4. Ejecutar el script:

python3 SeloS.py

📱 TERMUX

pkg update && pkg upgrade -y  
pkg install python git -y  
git clone https://github.com/DozerMx/SeloS.git  
cd SeloS
pip install -r requirements.txt  
python SeloS.py

------------------------------------------------------------
🚀 USO
------------------------------------------------------------

Ejecutar:

python3 SeloS.py

El script solicitará:

Target URL >> http://example.com  
Workers (100-10000) >> 1000

El ataque comenzará y mostrará el estado de las respuestas HTTP.

Ejemplo de salida:

Starting attack with 1000 workers against:  
http://example.com  
ATTACK IN PROGRESS...  
Press Ctrl+C to stop

------------------------------------------------------------
🔬 FUNCIONAMIENTO INTERNO
------------------------------------------------------------

- Usa asyncio para tareas concurrentes.
- ClientSession de aiohttp para lanzar múltiples requests.
- Headers dinámicos (User-Agent, Referer, Language).
- Rutas aleatorias tipo `/api`, `/login`, `/user/123`, etc.
- Manejo de concurrencia con asyncio.Semaphore.
- Salida visual con colores ANSI y figlet.

------------------------------------------------------------
⚖️ ADVERTENCIA LEGAL
------------------------------------------------------------

> ⚠️ Este script es solo para uso educativo y pruebas controladas.
> Ejecutarlo contra sistemas sin consentimiento es ILEGAL.
> Úsalo únicamente en servidores propios o con permiso explícito.

------------------------------------------------------------
👤 AUTOR
------------------------------------------------------------

- Nombre: DozerMx  
- Contacto: Telegram o GitHub  
- Versión: 1.0  
- Licencia: MIT  

------------------------------------------------------------
🛡️ DISCLAIMER
------------------------------------------------------------

El autor NO se hace responsable por el uso malicioso o ilegal de esta herramienta.  
El uso indebido puede resultar en consecuencias legales.  
USO BAJO TU PROPIO RIESGO.

================================
