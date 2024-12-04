import os
import shutil

def organizar_carpeta(ruta_carpeta):
    """
    Organiza los archivos en la carpeta especificada en subcarpetas según su tipo.
    
    Args:
        ruta_carpeta (str): Ruta de la carpeta a organizar.
    """
    # Diccionario con las extensiones y subcarpetas
    subcarpetas = {
        "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Programas": [".exe", ".msi"],
        "Comprimidos": [".zip", ".rar", ".7z"],
        "Otros": []
    }
    
    # Recorre los archivos en la carpeta especificada
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        
        # Verifica si es un archivo
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            movido = False
            
            # Busca la extensión en las subcarpetas
            for subcarpeta, extensiones in subcarpetas.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(ruta_carpeta, subcarpeta)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    movido = True
                    break
            
            # Si no coincide con ninguna extensión, mueve a "Otros"
            if not movido:
                carpeta_destino = os.path.join(ruta_carpeta, "Otros")
                os.makedirs(carpeta_destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

if __name__ == "__main__":
    # Pide al usuario la ruta de la carpeta a organizar
    ruta = input("Introduce la ruta de la carpeta que deseas organizar: ").strip()
    
    # Verifica si la ruta proporcionada es válida
    if os.path.isdir(ruta):
        organizar_carpeta(ruta)
        print(f"Se ha organizado la carpeta: {ruta}")
    else:
        print("La ruta proporcionada no es válida. Por favor, verifica e intenta de nuevo.")
