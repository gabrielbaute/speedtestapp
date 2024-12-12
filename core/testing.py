import speedtest
from datetime import datetime, timezone
from database.db import log_error, save_test_result

st = speedtest.Speedtest()

def get_upload():
    try:
        return st.upload() / 1000000
    except speedtest.SpeedtestUploadError as e:
        error_message=f"Error al medir la velocidad de subida: {e}"
        print(error_message)
        log_error(error_message)
        return None

def get_download():
    try:
        return st.download() / 1000000
    except speedtest.SpeedtestDownloadError as e:
        error_message=f"Error al medir la velocidad de descarga: {e}"
        print(error_message)
        log_error(error_message)
        return None

def get_best_server():
    try:
        return st.get_best_server()
    except speedtest.SpeedtestBestServerFailure as e:
        error_message=f"Error al obtener el mejor servidor: {e}"
        print(error_message)
        log_error(error_message)
        return None

def save_results():
    try:
        best = get_best_server()
        if best is None:
            error_message = "No se pudo obtener el mejor servidor."
            print(error_message)
            log_error(error_message)
            return
        
        upload = get_upload()
        if upload is None:
            error_message = "No se pudo obtener la velocidad de subida."
            print(error_message)
            log_error(error_message)
            return
        
        download = get_download()
        if download is None:
            error_message = "No se pudo obtener la velocidad de descarga."
            print(error_message)
            log_error(error_message)
            return
        
        latency = best["latency"]
        isp = best["sponsor"]
        city = best["name"]
        country = best["country"]
        
        save_test_result(upload, download, latency, isp, city, country, datetime.now(timezone.utc))  # Guardar en UTC
        print("Resultados guardados correctamente.")
    except Exception as e:
        error_message = f"Error inesperado: {e}"
        print(error_message)
        log_error(error_message)
