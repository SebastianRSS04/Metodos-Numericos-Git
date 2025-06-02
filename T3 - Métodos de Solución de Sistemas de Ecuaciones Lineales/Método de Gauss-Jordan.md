# Tema 3: Método de Gauss-Jordan

## Introducción al método de Gauss-Jordan 

El método de Gauss-Jordan es un paso más allá al transformar la matriz aumentada del sistema no solo a una forma escalonada, sino a una forma reducida by filas (también conocida como canónica) , dejando una matriz diagonal.


Este método permite obtener directamente la solución del sistema sin necesidad de aplicar la sustitución regresiva, lo cual lo hace más directo. Además, resulta particularmente útil cuando se desea invertir una matriz o resolver múltiples sistemas con la misma matriz de coeficientes, ya que su algoritmo transforma la matriz completa.

A pesar de su precisión y generalidad, el método de Gauss-Jordan tiene un costo computacional mayor que el de la eliminación gaussiana. Su complejidad lo vuelve poco práctico para sistemas de gran tamaño, donde los métodos iterativos o variantes optimizadas resultan más eficientes. No obstante, es una excelente herramienta didáctica y útil para comprender en profundidad la naturaleza algebraica de los sistemas lineales.

---

### Ventajas y Desventajas

**Ventajas:**
- Proporciona la solución directamente sin necesidad de sustitución regresiva.
- Es útil para invertir matrices o resolver múltiples sistemas con la misma matriz de coeficientes.
- Su forma reducida por filas facilita la interpretación de sistemas inconsistentes o con infinitas soluciones.

**Desventajas:**
- Tiene un costo computacional mayor que la eliminación gaussiana, especialmente en sistemas grandes.
- Puede ser sensible a errores de redondeo en sistemas mal condicionados.
- No incluye pivoteo por defecto, lo que puede requerir ajustes para mejorar la estabilidad numérica.

---

### Pseudocódigo

```text
Inicio
  Definir n como entero
  Definir A como matriz de reales [n][n]
  Definir b como vector de reales [n]
  Definir x como vector de reales [n]
  Definir i, j, k como enteros
  Definir factor como real

  n = 3
  A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
  b = [1, -2, 0]

  // Eliminación hacia adelante y hacia atrás
  Para k = 0 hasta n-1
    Si A[k][k] = 0
      Imprimir "Pivote nulo, no se puede resolver"
      Retornar
    Fin Si
    // Normalizar fila k
    factor = A[k][k]
    Para j = 0 hasta n-1
      A[k][j] = A[k][j] / factor
    Fin Para
    b[k] = b[k] / factor

    // Eliminar columna k en otras filas
    Para i = 0 hasta n-1
      Si i != k
        factor = A[i][k]
        Para j = 0 hasta n-1
          A[i][j] = A[i][j] - factor * A[k][j]
        Fin Para
        b[i] = b[i] - factor * b[k]
      Fin Si
    Fin Para
  Fin Para

  // Solución
  Para i = 0 hasta n-1
    x[i] = b[i]
  Fin Para

  Imprimir "Solución:"
  Para i = 0 hasta n-1
    Imprimir "x", i, " = ", x[i]
  Fin Para
Fin
```

### Código base en Java

```java
public class CodigoBaseGaussJordan {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = new double[n];

        // Eliminación hacia adelante y hacia atrás
        for (int k = 0; k < n; k++) {
            if (A[k][k] == 0) {
                System.out.println("Pivote nulo, no se puede resolver");
                return;
            }
            // Normalizar fila k
            double factor = A[k][k];
            for (int j = 0; j < n; j++) {
                A[k][j] /= factor;
            }
            b[k] /= factor;

            // Eliminar columna k en otras filas
            for (int i = 0; i < n; i++) {
                if (i != k) {
                    factor = A[i][k];
                    for (int j = 0; j < n; j++) {
                        A[i][j] -= factor * A[k][j];
                    }
                    b[i] -= factor * b[k];
                }
            }
        }

        // Solución
        for (int i = 0; i < n; i++) {
            x[i] = b[i];
        }

        // Imprimir solución
        System.out.println("Solución:");
        for (int i = 0; i < n; i++) {
            System.out.println("x" + i + " = " + x[i]);
        }
    }
}
```

### Ejemplo funcional en Java

```java
public class GaussJordan {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = new double[n];

        // Eliminación hacia adelante y hacia atrás
        for (int k = 0; k < n; k++) {
            if (A[k][k] == 0) {
                System.out.println("Pivote nulo, no se puede resolver");
                return;
            }
            // Normalizar fila k
            double factor = A[k][k];
            for (int j = 0; j < n; j++) {
                A[k][j] /= factor;
            }
            b[k] /= factor;

            // Eliminar columna k en otras filas
            for (int i = 0; i < n; i++) {
                if (i != k) {
                    factor = A[i][k];
                    for (int j = 0; j < n; j++) {
                        A[i][j] -= factor * A[k][j];
                    }
                    b[i] -= factor * b[k];
                }
            }
        }

        // Solución
        for (int i = 0; i < n; i++) {
            x[i] = b[i];
        }

        // Imprimir solución
        System.out.println("Solución:");
        for (int i = 0; i < n; i++) {
            System.out.printf("x%d = %.3f%n", i, x[i]);
        }
    }
}
```

### Caso de prueba:

```text
Solución:
x0 = 0.429
x1 = 0.143
x2 = -0.429
```
### [<- Regresar a T3 - Métodos de Solución de Sistemas de Ecuaciones Lineales ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T3%20-%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Sistemas%20de%20Ecuaciones%20Lineales/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Sistemas%20de%20Ecuaciones%20Lineales.md)
