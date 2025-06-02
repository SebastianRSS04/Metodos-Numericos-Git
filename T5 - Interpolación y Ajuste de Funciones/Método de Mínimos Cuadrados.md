# Tema 5: Método de Mínimos Cuadrados

## Introducción 

El método de mnimos cuadrados es una técnica poderosa para encontrar la función que mejor se ajusta a un conjunto de datos en el sentido de minimizar la suma de los cuadrados de los errores . El enfoque más comun es el alución más "óptima" bajo ciertos supuestos estadísticos, lo que lo convierte en una herramienta estándar en el análisis de datos y en el modelado de fenómenos experimentales.

Además de su versión lineal, el método de mínimos cuadrados puede extenderse a modelos polinómicos o incluso no lineales, con ayuda de herramientas computacionales. Es una técnica fundamental que no solo permite crear modelos predictivos, sino también comprender mejor las relaciones entre variables y evaluar el grado de ajuste de un modelo a la realidad observada.

---

### Ventajas y Desventajas

**Ventajas:**
- Proporciona el mejor ajuste lineal en términos de minimización del error cuadrático.
- Fácil de implementar y computacionalmente eficiente para modelos lineales.
- Ampliamente aplicable en ciencias, ingeniería y análisis de datos.

**Desventajas:**
- Sensible a valores atípicos, que pueden distorsionar el ajuste de la recta.
- Asume una relación lineal, lo que puede no ser adecuado para datos con patrones no lineales.
- Requiere cuidado en la interpretación si los datos no cumplen supuestos estadísticos (como normalidad de errores).

---

### Pseudocódigo

```text
Inicio
  Definir x como vector de reales [n]
  Definir y como vector de reales [n]
  Definir n como entero
  Definir sumX, sumY, sumXY, sumX2 como reales
  Definir m, b como reales
  Definir i como entero

  x = [0, 1, 2, 3]
  y = [1, 2.718, 7.389, 20.085]
  n = 4
  sumX = 0
  sumY = 0
  sumXY = 0
  sumX2 = 0

  Para i = 0 hasta n-1
    sumX = sumX + x[i]
    sumY = sumY + y[i]
    sumXY = sumXY + x[i] * y[i]
    sumX2 = sumX2 + x[i] * x[i]
  Fin Para

  m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX)
  b = (sumY - m * sumX) / n

  Imprimir "Ecuación de la recta: y = ", m, "x + ", b
Fin
```

---

### Código base en Java

```java
public class CodigoBaseLeastSquares {
    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};
        int n = x.length;
        double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
        }

        double m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        double b = (sumY - m * sumX) / n;

        System.out.println("Ecuación de la recta: y = " + m + "x + " + b);
    }
}
```

---

### Ejemplo funcional en Java

```java
public class LeastSquares {
    public static class LinearModel {
        public final double m; // Pendiente
        public final double b; // Intersección
        public final double mse; // Error cuadrático medio

        public LinearModel(double m, double b, double mse) {
            this.m = m;
            this.b = b;
            this.mse = mse;
        }
    }

    public static LinearModel fitLinearModel(double[] x, double[] y) {
        if (x == null || y == null || x.length != y.length || x.length < 2) {
            throw new IllegalArgumentException("Los vectores x e y deben tener la misma longitud y al menos 2 elementos");
        }

        int n = x.length;
        double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
        }

        double denominator = n * sumX2 - sumX * sumX;
        if (Math.abs(denominator) < 1e-10) {
            throw new IllegalArgumentException("No se puede ajustar la recta: datos insuficientes o colineales");
        }

        double m = (n * sumXY - sumX * sumY) / denominator;
        double b = (sumY - m * sumX) / n;

        // Calcular el error cuadrático medio (MSE)
        double mse = 0;
        for (int i = 0; i < n; i++) {
            double predicted = m * x[i] + b;
            mse += Math.pow(y[i] - predicted, 2);
        }
        mse /= n;

        return new LinearModel(m, b, mse);
    }

    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};

        try {
            LinearModel model = fitLinearModel(x, y);
            System.out.printf("Ajuste por mínimos cuadrados:%n");
            System.out.printf("Ecuación de la recta: y = %.3fx + %.3f%n", model.m, model.b);
            System.out.printf("Error cuadrático medio: %.3f%n", model.mse);
            System.out.println("Datos utilizados:");
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
Ajuste por mínimos cuadrados:
Ecuación de la recta: y = 6.361x + 0.171
Error cuadrático medio: 7.687
Datos utilizados:
(0.0, 1.000)
(1.0, 2.718)
(2.0, 7.389)
(3.0, 20.085)
```
### [<- T5 - Interpolación y Ajuste de Funciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T5%20-%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones/Introducci%C3%B3n%20a%20la%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones.md)
