# Tema 6: Método de un paso

## Introducción

Los métodos de un paso constituyen una clase fundamental de técnicas numéricas para resolver ecuaciones diferenciales ordinarias. Su característica principal es que el valor de la solución en el siguiente punto depende únicamente del valor en el punto actual. Es decir, no requieren almacenar o utilizar información de pasos anteriores, lo que los hace simples de implementar y controlar.

Un ejemplo clásico de este enfoque es el método de Euler, que utiliza una aproximación lineal basada en la derivada de la función para avanzar de un punto al siguiente. También se incluyen aquí variantes más precisas como el método de Heun y el método de Runge-Kutta. Estos métodos mejoran la precisión del método de Euler al considerar evaluaciones adicionales de la función derivada dentro del mismo paso.

Aunque los métodos de un paso son conceptualmente simples y adecuados para una amplia gama de problemas, pueden requerir pasos pequeños para mantener la estabilidad y precisión, especialmente en ecuaciones rígidas. Aun así, siguen siendo herramientas muy poderosas y son la base de muchos algoritmos más complejos en el análisis numérico.

---

### Ventajas y Desventajas

**Ventajas:**
- Simples de implementar y entender, ideales para problemas básicos.
- No requieren almacenar información de pasos anteriores, lo que reduce el uso de memoria.
- Flexibles para ecuaciones diferenciales de diferentes tipos.

**Desventajas:**
- Menos precisos que los métodos de pasos múltiples para el mismo número de evaluaciones.
- Pueden ser inestables para pasos grandes o ecuaciones rígidas.
- Requieren pasos pequeños para lograr alta precisión, aumentando el costo computacional.

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
  Definir k1, k2 como reales

  a = 0.0
  b = 1.0
  h = 0.2
  n = 5
  y[0] = 1.0

  Para i = 0 hasta n
    x[i] = a + i * h
  Fin Para

  Para i = 0 hasta n-1
    k1 = f(x[i], y[i])
    k2 = f(x[i] + h, y[i] + h * k1)
    y[i+1] = y[i] + (h / 2) * (k1 + k2)
  Fin Para

  Para i = 0 hasta n
    Imprimir "x = ", x[i], ", y = ", y[i]
  Fin Para
Fin
```

---

### Código base en Java

```java
public class CodigoBaseHeunMethod {
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

        for (int i = 0; i < n; i++) {
            double k1 = f(x[i], y[i]);
            double k2 = f(x[i] + h, y[i] + h * k1);
            y[i + 1] = y[i] + (h / 2) * (k1 + k2);
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
public class HeunMethod {
    public static class SolutionPoint {
        public final double x;
        public final double y;

        public SolutionPoint(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static SolutionPoint[] solveHeun(double a, double b, double h, double y0) {
        if (a >= b || h <= 0) {
            throw new IllegalArgumentException("El intervalo debe ser a < b y h debe ser positivo");
        }

        int n = (int) Math.ceil((b - a) / h);
        if (n < 1) {
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

        // Método de Heun
        for (int i = 0; i < n; i++) {
            double k1 = f(x[i], y[i]);
            double k2 = f(x[i] + h, y[i] + h * k1);
            y[i + 1] = y[i] + (h / 2) * (k1 + k2);
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
            SolutionPoint[] solution = solveHeun(a, b, h, y0);
            System.out.printf("Método de Heun (Runge-Kutta de orden 2):%n");
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
Método de Heun (Runge-Kutta de orden 2):
Ecuación diferencial: dy/dx = -2xy
Condición inicial: y(0.0) = 1.000
Intervalo: [0.0, 1.0], h = 0.2
Resultados:
x = 0.0, y = 1.000
x = 0.2, y = 0.992
x = 0.4, y = 0.938
x = 0.6, y = 0.826
x = 0.8, y = 0.683
x = 1.0, y = 0.548
```
### [<- T6 - Solución de Ecuaciones Diferenciales ](https://github.com/Yayackie/Trabajos_Metodos-Numericos/blob/main/T6%20-%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales/Introducci%C3%B3n%20a%20la%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales.md)
