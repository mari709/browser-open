import webbrowser
import time

def abrir_pagina(url):
    try:
        webbrowser.open(url)
        print(f"Página abierta exitosamente: {url}")
    except Exception as e:
        print(f"Error al abrir la página: {e}")

if __name__ == "__main__":
    # URL de la página que deseas abrir
    url = 'https://www.google.com'

    try:
        while True:
            # Abrir la página en el navegador predeterminado
            abrir_pagina(url)

            # Esperar 15 minutos antes de volver a abrir la página
            time.sleep(900)  # 900 segundos = 15 minutos

    except KeyboardInterrupt:
        # Manejar la interrupción del teclado (Ctrl+C)
        print("Script interrumpido por el usuario.")