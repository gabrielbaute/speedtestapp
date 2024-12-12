# Speed Test App

Este proyecto es una aplicación web para monitorear y visualizar las velocidades de subida y bajada de tu conexión a Internet, así como la latencia. La aplicación está construida con Flask y utiliza Chart.js para la visualización de datos. El proyecto está inspirado en SpeedTest Tracker, otro proyecto genial y que me encanta. El principal problema es que, lamentablemente, ese proyecto sólo se ejecuta en docker o en linux, y ejecutar docker en Windows implica un gran consumo de recursos (y trabajo con equipos de media-baja gama, por lo que cada Gb de la RAM es muy valioso para mi). En ese sentido, quise emprender este proyecto para buscar la manera de ejecutar una función similar en un entorno Windows. Aún me queda mucho por aprender, pero espero lograr el reto de ejecutar esta pequeña app en mi propia PC.

PD: la solución a todos mis problemas parece ser obvia: desinstala Windows, pero me gusta complicarme la vida.

## Requisitos

- Python 3.8+
- Flask
- SQLAlchemy
- Speedtest-cli
- Chart.js

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/gabrielbaute/speedtestapp
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd speedtest-app
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En Mac/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Configura la base de datos y guarda los resultados del test de velocidad ejecutando el script `testing.py`.
2. Inicia la aplicación Flask:
    ```bash
    flask run
    ```
3. Abre tu navegador y navega a `http://localhost:5505` para ver la aplicación en acción.

## Logging

La aplicación registra los errores en un archivo `error.log` en el directorio raíz del proyecto.

## Generación de Ejecutable

Para generar un archivo .exe que se ejecute en segundo plano:
1. Instala PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2. Genera el ejecutable:
    ```bash
    pyinstaller --onefile --name=SpeedTestApp main.py
    ```
3. Ejecuta el archivo .exe generado para iniciar la aplicación en segundo plano. Esta parte, por ahora, aún me está dando problemas, pronto corregiremos y daremos más información sobre cómo crear y utilizar los ejecutables.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request en el repositorio. Cualquier comentario o ayuda es bienvenida!

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
