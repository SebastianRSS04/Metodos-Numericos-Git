# Metodo de Regresión 

## Introducción 

El método de regresión es una técnica estadstica que se utiliza para modelar la relación entre una variable dependiente y una o más variables independientes . A diferencia de la interpolación, la regresión no busca pasar exactamente por todos los puntos, sino obtener una función representativa, donde se ajusta una línea recta a los datos minimizando el error cuadrático entre los valores observados y los estimados. Existen también regresiones polinómicas, logarítmicas, exponenciales y otros modelos que se adaptan a distintas situaciones según la naturaleza del fenómeno observado.

El método de regresión es ampliamente utilizado en diversas disciplinas como economía, física, ingeniería y ciencias sociales, ya que permite hacer predicciones, analizar relaciones entre variables y evaluar la fuerza y dirección de estas relaciones. Es un pilar fundamental del análisis estadístico y del modelado matemático basado en datos reales.

---

### Ventajas y Desventajas

**Ventajas:**
- Modela tendencias generales en datos ruidosos o dispersos, útil para predicciones.
- Proporciona métricas (como \( R^2 \)) para evaluar la calidad del ajuste.
- Flexible, aplicable a modelos lineales y no lineales con las adaptaciones adecuadas.

**Desventajas:**
- Sensible a valores atípicos, que pueden distorsionar el modelo.
- Asume una relación específica (lineal en este caso), lo que puede no ser adecuado para datos complejos.
- Requiere supuestos estadísticos (como independencia de errores) que no siempre se cumplen.

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
public class CodigoBaseLinearRegression {
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
public class LinearRegression {
    public static class RegressionModel {
        public final double m; // Pendiente
        public final double b; // Intersección
        public final double rSquared; // Coeficiente de determinación
        public final double mse; // Error cuadrático medio

        public RegressionModel(double m, double b, double rSquared, double mse) {
            this.m = m;
            this.b = b;
            this.rSquared = rSquared;
            this.mse = mse;
        }
    }

    public static RegressionModel fitLinearRegression(double[] x, double[] y) {
        if (x == null || y == null || x.length != y.length || x.length < 2) {
            throw new IllegalArgumentException("Los vectores x e y deben tener la misma longitud y al menos 2 elementos");
        }

        int n = x.length;
        double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0, sumY2 = 0;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
            sumY2 += y[i] * y[i];
        }

        double denominator = n * sumX2 - sumX * sumX;
        if (Math.abs(denominator) < 1e-10) {
            throw new IllegalArgumentException("No se puede ajustar la recta: datos insuficientes o colineales");
        }

        double m = (n * sumXY - sumX * sumY) / denominator;
        double b = (sumY - m * sumX) / n;

        // Calcular el coeficiente de determinación (R^2)
        double yMean = sumY / n;
        double ssTot = 0, ssRes = 0;
        for (int i = 0; i < n; i++) {
            double yPred = m * x[i] + b;
            ssRes += Math.pow(y[i] - yPred, 2);
            ssTot += Math.pow(y[i] - yMean, 2);
        }
        double rSquared = ssTot > 1e-10 ? 1 - ssRes / ssTot : 0;
        double mse = ssRes / n;

        return new RegressionModel(m, b, rSquared, mse);
    }

    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};

        try {
            RegressionModel model = fitLinearRegression(x, y);
            System.out.printf("Regresión lineal simple:%n");
            System.out.printf("Ecuación de la recta: y = %.3fx + %.3f%n", model.m, model.b);
            System.out.printf("Coeficiente de determinación (R^2): %.3f%n", model.rSquared);
            System.out.printf("Error cuadrático medio (MSE): %.3f%n", model.mse);
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
Regresión lineal simple:
Ecuación de la recta: y = 6.361x + 0.171
Coeficiente de determinación (R^2): 0.818
Error cuadrático medio (MSE): 7.687
Datos utilizados:
(0.0, 1.000)
(1.0, 2.718)
(2.0, 7.389)
(3.0, 20.085)
```
### [<- T5 - Interpolación y Ajuste de Funciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T5/Introducci%C3%B3n%20a%20la%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones.md)
