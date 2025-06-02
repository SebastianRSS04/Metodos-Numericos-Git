# Tema 5: Interpolación Polinómica

## Introducción 

La interpolación polinómica busca construir un polinomio de grado n + 1 puntos conocidos , ya que emplea expresiones matemáticas más ricas en términos de comportamiento.

Los datos, pero utilizan distintas formulaciones para hacerlo. Estos métodos se consideran exactos para los puntos conocidos, pero pueden presentar problemas de oscilación (conocido como fenómeno de Runge) cuando se utilizan polinomios de alto grado en intervalos amplios.

La interpolación polinómica es especialmente valiosa cuando se tiene un número moderado de datos distribuidos uniformemente y se busca una función que se adapte con exactitud. Sin embargo, en aplicaciones con muchos datos, suelen preferirse métodos alternativos como los splines o el ajuste de funciones, para evitar inestabilidad numérica.

---

### Ventajas y Desventajas

**Ventajas:**
- Captura mejor la curvatura de funciones complejas en comparación con la interpolación lineal.
- Proporciona resultados exactos en los puntos conocidos.
- Útil para modelar datos con un número moderado de puntos.

**Desventajas:**
- Puede generar oscilaciones significativas (fenómeno de Runge) con polinomios de alto grado.
- Computacionalmente más costoso que la interpolación lineal.
- Menos robusto para datos con ruido o distribuciones no uniformes.

---

### Pseudocódigo

```text
Inicio
  Definir x como vector de reales [n]
  Definir y como vector de reales [n]
  Definir xp como real
  Definir yp como real
  Definir L como real
  Definir i, j como enteros

  x = [0, 1, 2, 3]
  y = [1, 2.718, 7.389, 20.085]
  xp = 1.5
  n = 4
  yp = 0

  Para i = 0 hasta n-1
    L = 1
    Para j = 0 hasta n-1
      Si j != i
        L = L * (xp - x[j]) / (x[i] - x[j])
      Fin Si
    Fin Para
    yp = yp + y[i] * L
  Fin Para

  Imprimir "Valor interpolado en x = ", xp, ": ", yp
Fin
```

---

### Código base en Java

```java
public class CodigoBasePolynomialInterpolation {
    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};
        double xp = 1.5;
        int n = x.length;
        double yp = 0;

        for (int i = 0; i < n; i++) {
            double L = 1;
            for (int j = 0; j < n; j++) {
                if (j != i) {
                    L *= (xp - x[j]) / (x[i] - x[j]);
                }
            }
            yp += y[i] * L;
        }

        System.out.println("Valor interpolado en x = " + xp + ": " + yp);
    }
}
```

---

### Ejemplo funcional en Java

```java
public class PolynomialInterpolation {
    public static double interpolateLagrange(double[] x, double[] y, double xp) {
        if (x == null || y == null || x.length != y.length || x.length < 2) {
            throw new IllegalArgumentException("Los vectores x e y deben tener la misma longitud y al menos 2 elementos");
        }
        for (int i = 1; i < x.length; i++) {
            if (x[i] <= x[i - 1]) {
                throw new IllegalArgumentException("El vector x debe estar ordenado en orden ascendente");
            }
        }
        for (int i = 0; i < x.length; i++) {
            for (int j = i + 1; j < x.length; j++) {
                if (Math.abs(x[i] - x[j]) < 1e-10) {
                    throw new IllegalArgumentException("Los valores de x deben ser distintos");
                }
            }
        }

        double yp = 0;
        for (int i = 0; i < x.length; i++) {
            double L = 1;
            for (int j = 0; j < x.length; j++) {
                if (j != i) {
                    L *= (xp - x[j]) / (x[i] - x[j]);
                }
            }
            yp += y[i] * L;
        }
        return yp;
    }

    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};
        double xp = 1.5;

        try {
            double yp = interpolateLagrange(x, y, xp);
            System.out.printf("Interpolación polinómica (Lagrange):%n");
            System.out.printf("Punto interpolado: x = %.1f, y = %.3f%n", xp, yp);
            System.out.println("Puntos usados:");
            for (int i = 0; i < x.length; i++) {
                System.out.printf("(%.1f, %.3f)%n", x[i], y[i]);
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
Interpolación polinómica (Lagrange):
Punto interpolado: x = 1.5, y = 4.482
Puntos usados:
(0.0, 1.000)
(1.0, 2.718)
(2.0, 7.389)
(3.0, 20.085)
```
### [<- T5 - Interpolación y Ajuste de Funciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T5%20-%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones/Introducci%C3%B3n%20a%20la%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones.md)
