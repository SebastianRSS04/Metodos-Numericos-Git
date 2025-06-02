# Tema 6: Método de Pasos Múltiples

## Introducción

El método de pasos múltiples es una técnica numérica utilizada para resolver ecuaciones diferenciales ordinarias que, a diferencia de los métodos de un solo paso, utiliza información de varios puntos anteriores para calcular el valor siguiente de la solución. Esta estrategia permite mejorar la precisión sin requerir evaluaciones adicionales de la función derivada, lo que puede traducirse en un mejor rendimiento computacional.

Entre los métodos de pasos múltiples más conocidos se encuentran los métodos de Adams-Bashforth y Adams-Moulton. Estos métodos requieren una fase inicial de arranque, que generalmente se lleva a cabo con un método de un solo paso como Runge-Kutta, para calcular los primeros valores necesarios. Una vez establecidos estos valores iniciales, el método puede avanzar utilizando las evaluaciones previas.

La principal ventaja de los métodos de pasos múltiples es que ofrecen una mayor eficiencia en términos de precisión por evaluación de función. No obstante, también presentan desafíos, como la necesidad de gestionar condiciones iniciales múltiples y una mayor complejidad en su implementación. A pesar de esto, son ampliamente utilizados en aplicaciones donde se requiere integración a largo plazo con alta precisión.

---

### Ventajas y Desventajas

**Ventajas:**
- Mayor eficiencia computacional al reutilizar evaluaciones previas de la función.
- Alta precisión para ecuaciones diferenciales con comportamiento suave.
- Ideal para integraciones numéricas a largo plazo.

**Desventajas:**
- Requiere un método de arranque (como Euler o Runge-Kutta) para los primeros puntos.
- Más complejo de implementar que los métodos de un solo paso.
- Sensible a errores acumulados si las condiciones iniciales o el paso no son adecuados.

---

### Pseudocódigo

```text
Inicio
  Función f(x, y)
    Retornar -2 * x * y
  Fin Función

  Definir a como real
  Definir b como real
  Definir h como real
  Definir n como entero
  Definir x como vector de reales [n+1]
  Definir y como vector de reales [n+1]
  Definir i como entero

  a = 0.0
  b = 1.0
  h = 0.2
  n = 5
  y[0] = 1.0

  Para i = 0 hasta n
    x[i] = a + i * h
  Fin Para

  // Primer paso con Euler
  y[1] = y[0] + h * f(x[0], y[0])

  // Adams-Bashforth de 2 pasos
  Para i = 1 hasta n-1
    y[i+1] = y[i] + (h / 2) * (3 * f(x[i], y[i]) - f(x[i-1], y[i-1]))
  Fin Para

  Para i = 0 hasta n
    Imprimir "x = ", x[i], ", y = ", y[i]
  Fin Para
Fin
```

---

### Código base en Java

```java
public class CodigoBaseAdamsBashforth {
    public static double f(double x, double y) {
        return -2 * x * y;
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        double h = 0.2;
        int n = 5;
        double[] x = new double[n + 1];
        double[] y = new double[n + 1];
        y[0] = 1.0;

        for (int i = 0; i <= n; i++) {
            x[i] = a + i * h;
        }

        y[1] = y[0] + h * f(x[0], y[0]);

        for (int i = 1; i < n; i++) {
            y[i + 1] = y[i] + (h / 2) * (3 * f(x[i], y[i]) - f(x[i - 1], y[i - 1]));
        }

        for (int i = 0; i <= n; i++) {
            System.out.println("x = " + x[i] + ", y = " + y[i]);
        }
    }
}
```

---

### Ejemplo funcional en Java

```java
public class AdamsBashforth {
    public static class SolutionPoint {
        public final double x;
        public final double y;

        public SolutionPoint(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static SolutionPoint[] solveAdamsBashforth(double a, double b, double h, double y0) {
        if (a >= b || h <= 0) {
            throw new IllegalArgumentException("El intervalo debe ser a < b y h debe ser positivo");
        }

        int n = (int) Math.ceil((b - a) / h);
        if (n < 2) {
            throw new IllegalArgumentException("El paso h es demasiado grande para el intervalo");
        }

        double[] x = new double[n + 1];
        double[] y = new double[n + 1];
        SolutionPoint[] solution = new SolutionPoint[n + 1];

        // Inicializar puntos x
        for (int i = 0; i <= n; i++) {
            x[i] = a + i * h;
            if (i == n && Math.abs(x[i] - b) > 1e-10) {
                x[i] = b; // Ajustar el último punto al límite b
            }
        }

        // Condición inicial
        y[0] = y0;

        // Primer paso con Euler
        y[1] = y[0] + h * f(x[0], y[0]);

        // Adams-Bashforth de 2 pasos
        for (int i = 1; i < n; i++) {
            y[i + 1] = y[i] + (h / 2) * (3 * f(x[i], y[i]) - f(x[i - 1], y[i - 1]));
        }

        // Almacenar resultados
        for (int i = 0; i <= n; i++) {
            solution[i] = new SolutionPoint(x[i], y[i]);
        }

        return solution;
    }

    public static double f(double x, double y) {
        return -2 * x * y;
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        double h = 0.2;
        double y0 = 1.0;

        try {
            SolutionPoint[] solution = solveAdamsBashforth(a, b, h, y0);
            System.out.printf("Método de Adams-Bashforth (2 pasos):%n");
            System.out.printf("Ecuación diferencial: dy/dx = -2xy%n");
            System.out.printf("Condición inicial: y(%.1f) = %.3f%n", a, y0);
            System.out.printf("Intervalo: [%.1f, %.1f], h = %.1f%n", a, b, h);
            System.out.println("Resultados:");
            for (SolutionPoint point : solution) {
                System.out.printf("x = %.1f, y = %.3f%n", point.x, point.y);
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

---

### Caso de prueba:

```text
Método de Adams-Bashforth (2 pasos):
Ecuación diferencial: dy/dx = -2xy
Condición inicial: y(0.0) = 1.000
Intervalo: [0.0, 1.0], h = 0.2
Resultados:
x = 0.0, y = 1.000
x = 0.2, y = 1.000
x = 0.4, y = 0.960
x = 0.6, y = 0.862
x = 0.8, y = 0.711
x = 1.0, y = 0.574
```
### [<- T6 - Solución de Ecuaciones Diferenciales ](https://github.com/Yayackie/Trabajos_Metodos-Numericos/blob/main/T6%20-%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales/Introducci%C3%B3n%20a%20la%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales.md)
