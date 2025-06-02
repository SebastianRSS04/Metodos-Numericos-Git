# Tema 6: Método de Euler

## Introducción 

El método de Euler es uno de los algoritmos más simples y fundamentales para la resolución numérica de ecuaciones diferenciales ordinarias. Se basa en la idea de aproximar la curva solución mediante segmentos de recta tangente, utilizando la derivada en un punto dado para predecir.

Su facilidad de implementación, lo que lo convierte en una herramienta ideal para la enseñanza y el aprendizaje inicial del tema. Sin embargo, debido a que utiliza una única evaluación de la derivada por paso, su precisión puede ser baja, especialmente para intervalos grandes o funciones con comportamientos complejos.

A pesar de sus limitaciones, el método de Euler es la base para desarrollar métodos más avanzados y precisos. En la práctica, se usa principalmente para ilustrar principios o como paso inicial en métodos de pasos múltiples más complejos.

---

### Ventajas y Desventajas

**Ventajas:**
- Extremadamente simple de implementar y entender.
- Requiere una sola evaluación de la función derivada por paso, lo que lo hace computacionalmente ligero.
- Útil para fines educativos y como punto de partida para métodos más sofisticados.

**Desventajas:**
- Baja precisión (error de orden \( O(h) \)), lo que lo hace inadecuado para pasos grandes.
- Puede ser inestable para ecuaciones rígidas o problemas con derivadas grandes.
- Acumula errores rápidamente en integraciones a largo plazo.

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

  Para i = 0 hasta n-1
    y[i+1] = y[i] + h * f(x[i], y[i])
  Fin Para

  Para i = 0 hasta n
    Imprimir "x = ", x[i], ", y = ", y[i]
  Fin Para
Fin
```

---

### Código base en Java

```java
public class CodigoBaseEulerMethod {
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
            y[i + 1] = y[i] + h * f(x[i], y[i]);
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
public class EulerMethod {
    public static class SolutionPoint {
        public final double x;
        public final double y;

        public SolutionPoint(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static SolutionPoint[] solveEuler(double a, double b, double h, double y0) {
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

        // Método de Euler
        for (int i = 0; i < n; i++) {
            y[i + 1] = y[i] + h * f(x[i], y[i]);
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
            SolutionPoint[] solution = solveEuler(a, b, h, y0);
            System.out.printf("Método de Euler:%n");
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
Método de Euler:
Ecuación diferencial: dy/dx = -2xy
Condición inicial: y(0.0) = 1.000
Intervalo: [0.0, 1.0], h = 0.2
Resultados:
x = 0.0, y = 1.000
x = 0.2, y = 1.000
x = 0.4, y = 0.960
x = 0.6, y = 0.846
x = 0.8, y = 0.677
x = 1.0, y = 0.488
```
### [<- Regresar a T6 - Sistemas de Ecuaciones Diferenciales Ordinarias](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T6%20-%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales/Sistemas%20de%20Ecuaciones%20Diferenciales%20Ordinarias/Introducci%C3%B3n%20a%20los%20SIstemas%20de%20Ecuaciones%20Diferenciales%20Ordinarias.md)
