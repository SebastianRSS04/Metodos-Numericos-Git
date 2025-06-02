# Tema 3: Método de Gauss-Seidel

## Introducción al método de Gauss-Seidel 

El método de Gauss-Seidel es una técnica iterativa para resolver sistemas de ecuaciones lineales y mejora progresivamente dicha estimación utilizando las ecuaciones del sistema.

Para que funcione correctamente, el sistema debe cumplir ciertas condiciones de convergencia, como que la matriz de coeficientes sea diagonalmente dominante o simétrica positiva definida.

El método de Gauss-Seidel es fácil de implementar y puede alcanzar resultados precisos con pocos recursos computacionales si se cumplen las condiciones adecuadas. Sin embargo, no garantiza siempre la convergencia, por lo que es fundamental realizar un análisis previo del sistema o aplicar técnicas de precondicionamiento para asegurar su efectividad.

---

### Ventajas y Desventajas

**Ventajas:**
- Converge más rápido que el método de Jacobi al usar valores actualizados inmediatamente.
- Eficiente para sistemas grandes y dispersos, como los que aparecen en aplicaciones científicas.
- Requiere menos memoria que los métodos directos, ya que es iterativo.

**Desventajas:**
- La convergencia no está garantizada si la matriz no cumple condiciones como ser diagonalmente dominante.
- Puede ser sensible a la elección de la estimación inicial.
- En sistemas mal condicionados, puede requerir técnicas de precondicionamiento para converger.

---

### Pseudocódigo

```java
Inicio
  Definir n como entero
  Definir A como matriz de reales [n][n]
  Definir b como vector de reales [n]
  Definir x como vector de reales [n]
  Definir xNuevo como vector de reales [n]
  Definir tolerancia como real
  Definir maxIteraciones como entero
  Definir iteracion como entero
  Definir i, j como enteros
  Definir error como real

  n = 3
  A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
  b = [1, -2, 0]
  x = [0, 0, 0]
  tolerancia = 0.001
  maxIteraciones = 100
  iteracion = 0

  Mientras iteracion < maxIteraciones
    error = 0
    Para i = 0 hasta n-1
      Definir suma como real
      suma = 0
      Para j = 0 hasta n-1
        Si j != i
          suma = suma + A[i][j] * x[j]
        Fin Si
      Fin Para
      xNuevo[i] = (b[i] - suma) / A[i][i]
      error = max(error, abs(xNuevo[i] - x[i]))
      x[i] = xNuevo[i]
    Fin Para

    Imprimir "Iteración ", iteracion, ":"
    Para i = 0 hasta n-1
      Imprimir "x", i, " = ", x[i]
    Fin Para

    Si error < tolerancia
      Imprimir "Solución encontrada"
      Retornar
    Fin Si

    iteracion = iteracion + 1
  Fin Mientras

  Imprimir "Máximo de iteraciones alcanzado"
Fin
```

### Código base en Java

```java
public class CodigoBaseGaussSeidel {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = {0, 0, 0};
        double[] xNuevo = new double[n];
        double tolerancia = 0.001;
        int maxIteraciones = 100;
        int iteracion = 0;

        while (iteracion < maxIteraciones) {
            double error = 0;
            for (int i = 0; i < n; i++) {
                double suma = 0;
                for (int j = 0; j < n; j++) {
                    if (j != i) {
                        suma += A[i][j] * x[j];
                    }
                }
                xNuevo[i] = (b[i] - suma) / A[i][i];
                error = Math.max(error, Math.abs(xNuevo[i] - x[i]));
                x[i] = xNuevo[i];
            }

            System.out.println("Iteración " + iteracion + ":");
            for (int i = 0; i < n; i++) {
                System.out.println("x" + i + " = " + x[i]);
            }

            if (error < tolerancia) {
                System.out.println("Solución encontrada");
                return;
            }

            iteracion++;
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Ejemplo funcional en Java

```java
public class GaussSeidel {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = {0, 0, 0};
        double[] xNuevo = new double[n];
        double tolerancia = 0.001;
        int maxIteraciones = 100;

        for (int iteracion = 0; iteracion < maxIteraciones; iteracion++) {
            double error = 0;
            for (int i = 0; i < n; i++) {
                double suma = 0;
                for (int j = 0; j < n; j++) {
                    if (j != i) {
                        suma += A[i][j] * x[j];
                    }
                }
                xNuevo[i] = (b[i] - suma) / A[i][i];
                error = Math.max(error, Math.abs(xNuevo[i] - x[i]));
                x[i] = xNuevo[i];
            }

            System.out.printf("Iteración %d:%n", iteracion);
            for (int i = 0; i < n; i++) {
                System.out.printf("x%d = %.3f%n", i, x[i]);
            }

            if (error < tolerancia) {
                System.out.println("Solución encontrada");
                return;
            }
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Caso de prueba:

```java
Iteración 0:
x0 = 0.333
x1 = -0.667
x2 = -0.583

Iteración 1:
x0 = 0.583
x1 = 0.083
x2 = -0.458

Iteración 2:
x0 = 0.458
x1 = 0.121
x2 = -0.430

Iteración 3:
x0 = 0.430
x1 = 0.140
x2 = -0.429

Iteración 4:
x0 = 0.429
x1 = 0.143
x2 = -0.429

Solución encontrada
```
### [<- Regresar a T3 - Métodos de Solución de Sistemas de Ecuaciones Lineales ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T3/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Sistemas%20de%20Ecuaciones%20Lineales.md)
