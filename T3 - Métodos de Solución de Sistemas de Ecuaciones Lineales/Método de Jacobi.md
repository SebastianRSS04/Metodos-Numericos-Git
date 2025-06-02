# Tema 3: Método de Jacobi

## Introducción al método de Jacobi 

El método de Jacobi es a diferencia del método de Gauss-Seidel , el método de Jacobi calcula las nuevas aproximaciones de todas las variables nicamente los valores de la iteración anterior, sin actualizarlos en el mismo ciclo, 

Al igual que Gauss-Seidel, requiere que el sistema cumpla ciertas condiciones para garantizar la convergencia, como la dominancia diagonal. Sin embargo, suele converger más lentamente que Gauss-Seidel en la práctica.

A pesar de ser menos eficiente que otros métodos iterativos en muchos casos, el método de Jacobi sigue siendo relevante como base para el estudio de técnicas numéricas iterativas, y también es útil en contextos donde el paralelismo o la independencia entre procesos es esencial para el rendimiento computacional.

---

### Ventajas y Desventajas

**Ventajas:**
- Fácil de paralelizar debido a la independencia de las actualizaciones.
- Simple de implementar y adecuado para sistemas dispersos.
- Requiere poca memoria adicional al usar solo los valores anteriores.

**Desventajas:**
- Converge más lentamente que el método de Gauss-Seidel en la mayoría de los casos.
- No garantiza convergencia a menos que la matriz sea diagonalmente dominante.
- Puede requerir más iteraciones para alcanzar la tolerancia deseada.

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
    Para i = 0 hasta n-1
      Definir suma como real
      suma = 0
      Para j = 0 hasta n-1
        Si j != i
          suma = suma + A[i][j] * x[j]
        Fin Si
      Fin Para
      xNuevo[i] = (b[i] - suma) / A[i][i]
    Fin Para

    error = 0
    Para i = 0 hasta n-1
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
public class CodigoBaseJacobi {
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
            for (int i = 0; i < n; i++) {
                double suma = 0;
                for (int j = 0; j < n; j++) {
                    if (j != i) {
                        suma += A[i][j] * x[j];
                    }
                }
                xNuevo[i] = (b[i] - suma) / A[i][i];
            }

            double error = 0;
            for (int i = 0; i < n; i++) {
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
public class Jacobi {
    public static void main(String[] args) {
        int n = 3;
        double[][] A = {{3, 2, -1}, {2, -2, 4}, {-1, 0.5, -1}};
        double[] b = {1, -2, 0};
        double[] x = {0, 0, 0};
        double[] xNuevo = new double[n];
        double tolerancia = 0.001;
        int maxIteraciones = 100;

        for (int iteracion = 0; iteracion < maxIteraciones; iteracion++) {
            for (int i = 0; i < n; i++) {
                double suma = 0;
                for (int j = 0; j < n; j++) {
                    if (j != i) {
                        suma += A[i][j] * x[j];
                    }
                }
                xNuevo[i] = (b[i] - suma) / A[i][i];
            }

            double error = 0;
            for (int i = 0; i < n; i++) {
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
x1 = -1.000
x2 = 0.000

Iteración 1:
x0 = 0.667
x1 = -0.667
x2 = -0.167

Iteración 2:
x0 = 0.500
x1 = -0.167
x2 = -0.583

Iteración 3:
x0 = 0.583
x1 = 0.167
x2 = -0.333

Iteración 4:
x0 = 0.389
x1 = -0.083
x2 = -0.458

Iteración 5:
x0 = 0.458
x1 = 0.111
x2 = -0.403

Iteración 6:
x0 = 0.412
x1 = 0.042
x2 = -0.444

Iteración 7:
x0 = 0.429
x1 = 0.139
x2 = -0.423

Solución encontrada
```
### [<- Regresar a T3 - Métodos de Solución de Sistemas de Ecuaciones Lineales ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T3%20-%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Sistemas%20de%20Ecuaciones%20Lineales/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Sistemas%20de%20Ecuaciones%20Lineales.md)
