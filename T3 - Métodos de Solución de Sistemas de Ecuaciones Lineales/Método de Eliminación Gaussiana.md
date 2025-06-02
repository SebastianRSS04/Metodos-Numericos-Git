# Tema 3: Método de Eliminación Gaussiana

## Introducción al método de Eliminación Gaussiana 

El método de Eliminación Gaussiana es una técnica directa para resolver sistemas de ecuaciones lineales en una forma escalonada equivalente mediante operaciones elementales sobre las filas de la matriz aumentada . Estas operaciones incluyen el intercambio de fila, se puede aplicar el método de sustitución regresiva para hallar las soluciones del sistema.

Este método es ampliamente utilizado debido a su claridad conceptual y su aplicabilidad general. Es capaz de resolver cualquier sistema de ecuaciones lineales que tenga solución única, aunque también puede detectar sistemas inconsistentes o con infinitas soluciones si se aplica correctamente. La eliminación gaussiana es especialmente útil en sistemas pequeños o medianos, o cuando se necesita una solución exacta sin depender de iteraciones.

Sin embargo, su eficiencia disminuye considerablemente en sistemas muy grandes, ya que requiere una cantidad significativa de operaciones. Además, puede ser sensible a errores de redondeo en sistemas mal condicionados. Por esta razón, en entornos computacionales se suele acompañar de técnicas de pivoteo para mejorar la estabilidad numérica del método.

---

### Ventajas y Desventajas

**Ventajas:**
- Proporciona una solución exacta para sistemas de ecuaciones lineales con solución única.
- Es conceptualmente claro y fácil de implementar en sistemas pequeños o medianos.
- Puede identificar sistemas inconsistentes o con infinitas soluciones durante el proceso.

**Desventajas:**
- La eficiencia disminuye en sistemas muy grandes debido al alto costo computacional.
- Es sensible a errores de redondeo, especialmente en sistemas mal condicionados.
- No incluye pivoteo por defecto, lo que puede requerir ajustes adicionales para mayor estabilidad.

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

  // Eliminación hacia adelante
  Para k = 0 hasta n-2
    Si A[k][k] = 0
      Imprimir "Pivote nulo, no se puede resolver"
      Retornar
    Fin Si
    Para i = k+1 hasta n-1
      factor = A[i][k] / A[k][k]
      Para j = k hasta n-1
        A[i][j] = A[i][j] - factor * A[k][j]
      Fin Para
      b[i] = b[i] - factor * b[k]
    Fin Para
  Fin Para

  // Sustitución hacia atrás
  x[n-1] = b[n-1] / A[n-1][n-1]
  Para i = n-2 hasta 0 con paso -1
    Definir suma como real
    suma = 0
    Para j = i+1 hasta n-1
      suma = suma + A[i][j] * x[j]
    Fin Para
    x[i] = (b[i] - suma) / A[i][i]
  Fin Para

  Imprimir "Solución:"
  Para i = 0 hasta n-1
    Imprimir "x", i, " = ", x[i]
  Fin Para
Fin
```

### Código base en Java

```java
public class CodigoBaseEliminacionGaussiana {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = new double[n];

        // Eliminación hacia adelante
        for (int k = 0; k < n - 1; k++) {
            if (A[k][k] == 0) {
                System.out.println("Pivote nulo, no se puede resolver");
                return;
            }
            for (int i = k + 1; i < n; i++) {
                double factor = A[i][k] / A[k][k];
                for (int j = k; j < n; j++) {
                    A[i][j] -= factor * A[k][j];
                }
                b[i] -= factor * b[k];
            }
        }

        // Sustitución hacia atrás
        x[n - 1] = b[n - 1] / A[n - 1][n - 1];
        for (int i = n - 2; i >= 0; i--) {
            double suma = 0;
            for (int j = i + 1; j < n; j++) {
                suma += A[i][j] * x[j];
            }
            x[i] = (b[i] - suma) / A[i][i];
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
public class GaussianElimination {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = new double[n];

        // Eliminación hacia adelante
        for (int k = 0; k < n - 1; k++) {
            if (A[k][k] == 0) {
                System.out.println("Pivote nulo, no se puede resolver");
                return;
            }
            for (int i = k + 1; i < n; i++) {
                double factor = A[i][k] / A[k][k];
                for (int j = k; j < n; j++) {
                    A[i][j] -= factor * A[k][j];
                }
                b[i] -= factor * b[k];
            }
        }

        // Sustitución hacia atrás
        x[n - 1] = b[n - 1] / A[n - 1][n - 1];
        for (int i = n - 2; i >= 0; i--) {
            double suma = 0;
            for (int j = i + 1; j < n; j++) {
                suma += A[i][j] * x[j];
            }
            x[i] = (b[i] - suma) / A[i][i];
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
### [<- Regresar a T3 - Métodos de Solución de Sistemas de Ecuaciones Lineales ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T3/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Sistemas%20de%20Ecuaciones%20Lineales.md)
