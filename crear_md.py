import os

# Define la estructura con carpetas y archivos .md
estructura = {
    "T2": [
        "Introducción a los Métodos de Solución de Ecuaciones.md",
        "Método_de_Bisección.md",
        "Método_de_Newton-Rhapson.md",
        "Método_de_Punto_Fijo.md",
        "Método_de_la_Regla_Falsa.md",
        "Método_de_la_Secante.md",
    ],
    "T3": [
        "Introducción a los Métodos de Solución de Sistemas de Ecuaciones Lineales.md",
        "Método_de_Eliminación_Gaussiana.md",
        "Método_de_Gauss-Jordan.md",
        "Método_de_Gauss-Seidel.md",
        "Método_de_Jacobi.md",
    ],
    "T4": [
        "Introducción a la Diferenciación e Integración Numérica.md",
        "Método_de_Simpson_13.md",
        "Método_de_Simpson_38.md",
        "Método_de_la_Cuadratura_Gaussiana.md",
        "Método_del_Trapecio.md",
    ],
    "T5": [
        "Introducción a la Interpolación y Ajuste de Funciones.md",
        "Interpolación_Lineal.md",
        "Interpolación_Polinómica.md",
        "Método_de_Regresión.md",
        "Método_de_Correlación.md",
        "Método_de_Mínimos_Cuadrados.md",
    ],
    "T6": [
        "Introducción a la Solución de Ecuaciones Diferenciales.md",
        "Método_de_Pasos_Múltiples.md",
        "Método_de_un_paso.md",
        # Carpeta para sub-subtemas
        {
            "Sistemas de Ecuaciones Diferenciales Ordinarias": [
                "Método_de_Euler.md",
                "Método_de_Runge-Kutta.md",
                "Método_de_Taylor.md",
            ]
        },
    ],
}

def crear_archivo(ruta, nombre):
    path = os.path.join(ruta, nombre)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            # Escribe título base en el archivo
            titulo = nombre.replace(".md", "").replace("_", " ")
            f.write(f"# {titulo}\n\n")
        print(f"Archivo creado: {path}")
    else:
        print(f"Archivo ya existe: {path}")

def crear_estructura(base_path, estructura):
    for clave, archivos in estructura.items():
        carpeta = os.path.join(base_path, clave)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"Carpeta creada: {carpeta}")
        else:
            print(f"Carpeta ya existe: {carpeta}")
        for item in archivos:
            if isinstance(item, dict):
                # Subcarpeta con archivos dentro
                for subcarpeta, subarchivos in item.items():
                    subcarpeta_path = os.path.join(carpeta, subcarpeta)
                    if not os.path.exists(subcarpeta_path):
                        os.makedirs(subcarpeta_path)
                        print(f"Subcarpeta creada: {subcarpeta_path}")
                    else:
                        print(f"Subcarpeta ya existe: {subcarpeta_path}")
                    for archivo in subarchivos:
                        crear_archivo(subcarpeta_path, archivo)
            else:
                crear_archivo(carpeta, item)

if __name__ == "__main__":
    raiz = os.getcwd()  # Ejecutar en la raíz del repo
    crear_estructura(raiz, estructura)
