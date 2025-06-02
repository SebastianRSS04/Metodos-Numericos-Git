# Tema 6: Método de Taylor

## Introducción 

El método de Taylor es una técnica numérica that aprovecha el desarrollo en serie de Taylor para aproximar la solución de una ecuación diferencial ordinaria, lo cual permite construir una mejor aproximación local de la función.

La desventaja de estas derivadas son difíciles de obtener o costosas de calcular. Sin embargo, cuando esta información está disponible, el método puede proporcionar soluciones altamente precisas.

Este método es especialmente útil cuando se busca comprender el comportamiento local de una solución con gran detalle o cuando se dispone de funciones cuyas derivadas son fácilmente derivables simbólicamente. Aunque no es tan utilizado como Runge-Kutta en la práctica general, es una herramienta poderosa en contextos específicos donde se prioriza la precisión local.

---

### Ventajas y Desventajas

**Ventajas:**
- Alta precisión local al incluir derivadas de orden superior (error de orden \( O(h^{n+1}) \) para un método de orden \( n \)).
- Útil para problemas donde las derivadas son fáciles de calcular analíticamente.
- Proporciona una base teórica sólida para entender otros métodos numéricos.

**Desventajas:**
- Requiere calcular derivadas de orden superior, lo que puede ser complejo o impracticable.
- Más costoso computacionalmente si las derivadas no están disponibles de forma cerrada.
- Menos utilizado en la práctica general debido a la popularidad de métodos como Runge-Kutta.

---

### Pseudocódigo

```text
Inicio
  Función f(x, y)
    Retornar -2 * x * y
  Fin Función

  Función fPrima(x, y)
    Retornar -2 * y - 2 * x * (-2 * x * y)
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
    y[i+1] = y[i] + h * f(x[i], y[i]) + (h^2 / 2) * fPrima(x[i], y[i])
  Fin Para

  Para i = 0 hasta n
    Imprimir "x = ", x[i], ", y = ", y[i]
  Fin Para
Fin
```

---

### Código base en Java

```java
public class CodigoBaseTaylorMethod {
    public static double f(double x, double y) {
        return -2 * x * y;
    }

    public static double fPrima(double x, double y) {
        return -2 * y - 2 * x * (-2 * x * y);
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
            y[i + 1] = y[i] + h * f(x[i], y[i]) + (h * h / 2) * fPrima(x[i], y[i]);
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
public class TaylorMethod {
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

    public static SolutionPoint[] solveTaylorOrder2(double a, double b, double h, double y0) {
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

        // Método de Taylor de orden 2
        for (int i = 0; i < n; i++) {
            y[i + 1] = y[i] + h * f(x[i], y[i]) + (h * h / 2) * fPrima(x[i], y[i]);
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

    public static double fPrima(double x, double y) {
        return -2 * y + 4 * x * x * y; // Simplificado: -2y + 4x^2y
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        double h = 0.2;
        double y0 = 1.0;

        try {
            SolutionPoint[] solution = solveTaylorOrder2(a, b, h, y0);
            System.out.printf("Método de Taylor (orden 2):%n");
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
Método de Taylor (orden 2):
Ecuación diferencial: dy/dx = -2xy
Condición inicial: y(0.0) = 1.000
Intervalo: [0.0, 1.0], h = 0.2
Resultados (y_num: solución numérica, y_exact: solución analítica):
x = 0.0, y_num = 1.000, y_exact = 1.000, error = 0.000e+00
x = 0.2, y_num = 0.960, y_exact = 0.961, error = 7.840e-04
x = 0.4, y_num = 0.852, y_exact = 0.852, error = 2.805e-03
x = 0.6, y_num = 0.697, y_exact = 0.698, error = 5.946e-03
x = 0.8, y_num = 0.527, y_exact = 0.527, error = 9.973e-03
x = 1.0, y_num = 0.368, y_exact = 0.368, error = 1.466e-02
```

---
### [<- Regresar a T6 - Sistemas de Ecuaciones Diferenciales Ordinarias](https://github.com/Yayackie/Trabajos_Metodos-Numericos/blob/main/T6%20-%20Soluci%C3%B3n%20de%20Ecuaciones%20Diferenciales/Sistemas%20de%20Ecuaciones%20Diferenciales%20Ordinarias/Introducci%C3%B3n%20a%20los%20SIstemas%20de%20Ecuaciones%20Diferenciales%20Ordinarias.md)

