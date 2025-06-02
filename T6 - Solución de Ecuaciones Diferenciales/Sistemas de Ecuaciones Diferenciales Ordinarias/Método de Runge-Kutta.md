# Tema 6: Método de Runge-Kutta

## Introducción 

El método de Runge-Kutta representa una familia de técnicas diseadas para mejorar la precisión de las soluciones obtenidas in ecuaciones diferenciales ordinarias , que logra un balance entre exactitud y eficiencia computacional sin necesidad de calcular derivadas de orden superior. 

A pesar de ser más costoso computacionalmente que el método de Euler, ofrece una precisión mucho mayor, por lo que es ampliamente utilizado en aplicaciones científicas y de ingeniería.

Gracias a su estabilidad, precisión y facilidad de implementación, el método de Runge-Kutta es uno de los más empleados en la resolución de problemas reales. Su versatilidad le permite adaptarse fácilmente a sistemas de ecuaciones y ecuaciones de orden superior mediante la reducción adecuada del sistema.

---

### Ventajas y Desventajas

**Ventajas:**
- Alta precisión (error de orden \( O(h^4) \) para RK4), ideal para problemas complejos.
- Estable para una amplia gama de ecuaciones diferenciales.
- No requiere derivadas de orden superior, solo evaluaciones de la función derivada.

**Desventajas:**
- Más costoso computacionalmente que métodos más simples como Euler (cuatro evaluaciones por paso en RK4).
- Puede requerir pasos pequeños para ecuaciones rígidas, aunque es más robusto que Euler.
- Implementación más compleja que métodos de un paso más básicos.

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
  Definir k1, k2, k3, k4 como reales

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
    k2 = f(x[i] + h/2, y[i] + (h/2) * k1)
    k3 = f(x[i] + h/2, y[i] + (h/2) * k2)
    k4 = f(x[i] + h, y[i] + h * k3)
    y[i+1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
  Fin Para

  Para i = 0 hasta n
    Imprimir "x = ", x[i], ", y = ", y[i]
  Fin Para
Fin
```

---

### Código base en Java

```java
public class CodigoBaseRungeKutta {
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
            double k2 = f(x[i] + h/2, y[i] + (h/2) * k1);
            double k3 = f(x[i] + h/2, y[i] + (h/2) * k2);
            double k4 = f(x[i] + h, y[i] + h * k3);
            y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
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
public class RungeKutta {
    public static class SolutionPoint {
        public final double x;
        public final double y;
        public final double yExact; // Solución analítica

        public SolutionPoint(double x, double y, double yExact) {
            this.x = x;
            this.y = y;
            this.yExact = yExact;
        }
    }

    public static SolutionPoint[] solveRungeKutta4(double a, double b, double h, double y0) {
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

        // Método de Runge-Kutta de orden 4
        for (int i = 0; i < n; i++) {
            double k1 = f(x[i], y[i]);
            double k2 = f(x[i] + h/2, y[i] + (h/2) * k1);
            double k3 = f(x[i] + h/2, y[i] + (h/2) * k2);
            double k4 = f(x[i] + h, y[i] + h * k3);
            y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
        }

        // Almacenar resultados con solución analítica
        for (int i = 0; i <= n; i++) {
            double yExact = Math.exp(-x[i] * x[i]); // Solución analítica: y = e^(-x^2)
            solution[i] = new SolutionPoint(x[i], y[i], yExact);
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
            SolutionPoint[] solution = solveRungeKutta4(a, b, h, y0);
            System.out.printf("Método de Runge-Kutta (orden 4):%n");
            System.out.printf("Ecuación diferencial: dy/dx = -2xy%n");
            System.out.printf("Condición inicial: y(%.1f) = %.3f%n", a, y0);
            System.out.printf("Intervalo: [%.1f, %.1f], h = %.1f%n", a, b, h);
            System.out.println("Resultados (y_num: solución numérica, y_exact: solución analítica):");
            for (SolutionPoint point : solution) {
                System.out.printf("x = %.1f, y_num = %.3f, y_exact = %.3f, error = %.3e%n", 
                    point.x, point.y, point.yExact, Math.abs(point.y - point.yExact));
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
Método de Runge-Kutta (orden 4):
Ecuación diferencial: dy/dx = -2xy
Condición inicial: y(0.0) = 1.000
Intervalo: [0.0, 1.0], h = 0.2
Resultados (y_num: solución numérica, y_exact: solución analítica):
x = 0.0, y_num = 1.000, y_exact = 1.000, error = 0.000e+00
x = 0.2, y_num = 0.961, y_exact = 0.961, error = 1.984e-06
x = 0.4, y_num = 0.852, y_exact = 0.852, error = 2.275e-05
x = 0.6, y_num = 0.697, y_exact = 0.698, error = 7.161e-05
x = 0.8, y_num = 0.527, y_exact = 0.527, error = 1.138e-04
x = 1.0, y_num = 0.368, y_exact = 0.368, error = 1.168e-04
```

---
### [<- Regresar a T6 - Sistemas de Ecuaciones Diferenciales Ordinarias](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T6%20-%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales/Sistemas%20de%20Ecuaciones%20Diferenciales%20Ordinarias/Introducci%C3%B3n%20a%20los%20SIstemas%20de%20Ecuaciones%20Diferenciales%20Ordinarias.md)

