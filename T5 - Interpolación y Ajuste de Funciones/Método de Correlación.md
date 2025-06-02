# Tema 5: Método de Correlación

## Introducción 

El método de correlación se utiliza para medir la intensidad y dirección de la relación lineal entre dos variables cuantitativas . A diferencia de la regresión, que busca construir una función para predecir una variable a partir de otra, la correlación simplemente evala qué tan estrechamente relacionadas están las variables

Indica una fuerte correlación positiva, es decir, ambas variables tienden a aumentar juntas. Un valor cercano a -1 indica una correlación negativa, donde una variable aumenta mientras la otra disminuye. Un valor cercano a 0 indica una débil o inexistente relación lineal.

La correlación es útil en la etapa exploratoria de análisis de datos, ya que ayuda a identificar patrones y relaciones que podrían estudiarse más a fondo con otros métodos como la regresión. Es importante recordar que la correlación no implica causalidad, por lo que debe interpretarse con cuidado y en conjunto con el contexto del problema.

---

### Ventajas y Desventajas

**Ventajas:**
- Simple de calcular e interpretar, proporcionando una medida clara de la relación lineal.
- Útil para identificar patrones en la etapa exploratoria de análisis de datos.
- Aplicable en una amplia gama de disciplinas, como estadística, economía y ciencias sociales.

**Desventajas:**
- Solo mide relaciones lineales, ignorando relaciones no lineales o más complejas.
- Sensible a valores atípicos, que pueden distorsionar el coeficiente de correlación.
- No implica causalidad, lo que puede llevar a interpretaciones erróneas si no se considera el contexto.

---

### Pseudocódigo

```text
Inicio
  Definir x como vector de reales [n]
  Definir y como vector de reales [n]
  Definir n como entero
  Definir sumX, sumY, sumXY, sumX2, sumY2 como reales
  Definir r como real
  Definir i como entero

  x = [0, 1, 2, 3]
  y = [1, 2.718, 7.389, 20.085]
  n = 4
  sumX = 0
  sumY = 0
  sumXY = 0
  sumX2 = 0
  sumY2 = 0

  Para i = 0 hasta n-1
    sumX = sumX + x[i]
    sumY = sumY + y[i]
    sumXY = sumXY + x[i] * y[i]
    sumX2 = sumX2 + x[i] * x[i]
    sumY2 = sumY2 + y[i] * y[i]
  Fin Para

  r = (n * sumXY - sumX * sumY) / sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY))

  Imprimir "Coeficiente de correlación: ", r
Fin
```

---

### Código base en Java

```java
public class CodigoBaseCorrelation {
    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};
        int n = x.length;
        double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0, sumY2 = 0;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
            sumY2 += y[i] * y[i];
        }

        double r = (n * sumXY - sumX * sumY) / 
                   Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));

        System.out.println("Coeficiente de correlación: " + r);
    }
}
```

---

### Ejemplo funcional en Java

```java
public class Correlation {
    public static double calculatePearsonCorrelation(double[] x, double[] y) {
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

        double denominator = Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));
        if (Math.abs(denominator) < 1e-10) {
            throw new IllegalArgumentException("No se puede calcular la correlación: varianza cero o datos constantes");
        }

        double r = (n * sumXY - sumX * sumY) / denominator;
        return r;
    }

    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};

        try {
            double r = calculatePearsonCorrelation(x, y);
            System.out.printf("Análisis de correlación (Pearson):%n");
            System.out.printf("Coeficiente de correlación: %.3f%n", r);
            System.out.printf("Interpretación: %s%n", interpretCorrelation(r));
            System.out.println("Datos analizados:");
            for (int i = 0; i < x.length; i++) {
                System.out.printf("(%.1f, %.3f)%n", x[i], y[i]);
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private static String interpretCorrelation(double r) {
        if (r > 0.7) return "Fuerte correlación positiva";
        if (r > 0.3) return "Correlación positiva moderada";
        if (r > -0.3) return "Correlación débil o inexistente";
        if (r > -0.7) return "Correlación negativa moderada";
        return "Fuerte correlación negativa";
    }
}
```

---

### Caso de prueba:

```text
Análisis de correlación (Pearson):
Coeficiente de correlación: 0.904
Interpretación: Fuerte correlación positiva
Datos analizados:
(0.0, 1.000)
(1.0, 2.718)
(2.0, 7.389)
(3.0, 20.085)
```
### [<- T5 - Interpolación y Ajuste de Funciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T5/Introducci%C3%B3n%20a%20la%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones.md)
