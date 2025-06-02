import os
import zipfile
import shutil
import requests
from transformers import pipeline

# 1. Define tu ruta local
DESTINO_FINAL = r"D:\OneDrive\Documentos\GitHub\Metodos-Numericos-Git"

# 2. Descarga ZIP del repo externo
ZIP_URL = "https://github.com/Yayackie/Trabajos_Metodos-Numericos/archive/refs/heads/main.zip"
ZIP_PATH = "repo_temporal.zip"
TEMP_FOLDER = "repo_temporal"

# 3. Modelo de parafraseo
print("⏳ Cargando modelo de parafraseo...")
parafraseador = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def descargar_y_extraer():
    print("📦 Descargando y extrayendo repo de Yayackie...")
    with requests.get(ZIP_URL, stream=True) as r:
        with open(ZIP_PATH, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(TEMP_FOLDER)

def parafrasear(texto):
    if not texto.strip():
        return texto
    respuesta = parafraseador(texto, max_length=512, num_return_sequences=1)[0]['generated_text']
    return respuesta.strip()

def procesar_md(carpeta_fuente, carpeta_destino):
    for carpeta, _, archivos in os.walk(carpeta_fuente):
        if "README.md" in archivos:
            archivos.remove("README.md")
        relativos = carpeta.split(os.sep)
        if len(relativos) < 2:
            continue
        subdir = relativos[-1]
        destino = os.path.join(carpeta_destino, subdir)
        os.makedirs(destino, exist_ok=True)

        for archivo in archivos:
            if not archivo.endswith(".md"):
                continue
            origen = os.path.join(carpeta, archivo)
            with open(origen, encoding="utf-8") as f:
                contenido_original = f.read()

            lineas = contenido_original.split("\n")
            encabezado = lineas[0]
            cuerpo = "\n".join(lineas[1:])

            parafraseado = parafrasear(cuerpo[:500]) + "\n\n" + cuerpo[500:]  # Parafraseo parcial por seguridad

            nuevo_contenido = f"{encabezado}\n\n{parafraseado}"

            destino_archivo = os.path.join(destino, archivo)

            # Preview
            print(f"\n📄 Archivo: {destino_archivo}")
            print("-" * 40)
            print(nuevo_contenido[:300])
            print("...\n")
            confirmar = input("¿Sobrescribir este archivo? (s/n): ").strip().lower()
            if confirmar == "s":
                with open(destino_archivo, "w", encoding="utf-8") as f:
                    f.write(nuevo_contenido)
                print("✅ Guardado.")
            else:
                print("❌ Omitido.")

# 4. Ejecuta todo
if __name__ == "__main__":
    descargar_y_extraer()
    fuente = os.path.join(TEMP_FOLDER, "Trabajos_Metodos-Numericos-main")
    procesar_md(fuente, DESTINO_FINAL)

    # Limpieza
    os.remove(ZIP_PATH)
    shutil.rmtree(TEMP_FOLDER)
    print("\n🎉 ¡Proceso completado!")
