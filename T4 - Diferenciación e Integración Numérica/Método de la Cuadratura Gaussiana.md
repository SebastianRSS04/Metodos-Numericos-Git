# Tema 4: Método de la Cuadratura Gaussiana

## Introducción 

La cuadratura gaussiana es una técnica avanzada de integración numérica qui permite obtener una alta precisión en la aproximación de integrales definidas con un nmero reducido de evaluaciones de la función. 

El principio de este método se basa en calcular la integral como una suma ponderada de los valores de la función en ciertos puntos llamados "puntos de Gauss", los cuales no están distribuidos uniformemente. Estos puntos y sus respectivos pesos se obtienen a partir de los ceros de los polinomios ortogonales (como los de Legendre) sobre un intervalo específico. Esta propiedad permite que el método logre una precisión notable incluso usando pocos puntos de evaluación.

Gracias a su eficiencia y precisión, la cuadratura gaussiana es muy utilizada en problemas complejos donde se busca minimizar el costo computacional, como en simulaciones físicas, problemas de elementos finitos y cálculos científicos avanzados. No obstante, su implementación requiere mayor preparación que los métodos más básicos, ya que los puntos y pesos deben calcularse o consultarse previamente para cada número de nodos.

---

### Ventajas y Desventajas

**Ventajas:**
- Ofrece alta precisión con un número reducido de puntos de evaluación.
- Óptimo para integrales definidas sobre intervalos específicos.
- Muy eficiente en problemas computacionales complejos.

**Desventajas:**
- Requiere precalcular o consultar puntos y pesos de Gauss.
- Menos intuitivo y más difícil de implementar que métodos básicos.
- No es adecuado si los puntos y pesos no están bien definidos para el intervalo.

---

### Pseudocódigo

```text
Inicio
  Función f(x)
    Retornar exp(x)
  Fin Función

  Definir a como real
  Definir b como real
  Definir n como entero
  Definir puntos como vector de reales [n]
  Definir pesos como vector de reales [n]
  Definir suma como real
  Definir t como real
  Definir x como real
  Definir i como entero
  Definir integral como real

  a = 0.0
  b = 1.0
  n = 3
  puntos = [-0.774596669, 0.0, 0.774596669]
  pesos = [0.555555556, 0.888888889, 0.555555556]

  suma = 0
  Para i = 0 hasta n-1
    t = puntos[i]
    x = ((b - a) * t + (b + a)) / 2
    suma = suma + pesos[i] * f(x)
  Fin Para

  integral = ((b - a) / 2) * suma
  Imprimir "Integral aproximada: ", integral
Fin
```

### Código base en Java

```java
public class CodigoBaseGaussianQuadrature {
    public static double f(double x) {
        return Math.exp(x);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        int n = 3;
        double[] puntos = {-0.774596669, 0.0, 0.774596669};
        double[] pesos = {0.555555556, 0.888888889, 0.555555556};

        double suma = 0;
        for (int i = 0; i < n; i++) {
            double t = puntos[i];
            double x = ((b - a) * t + (b + a)) / 2;
            suma += pesos[i] * f(x);
        }

        double integral = ((b - a) / 2) * suma;
        System.out.println("Integral aproximada: " + integral);
    }
}
```

### Ejemplo funcional en Java

```java
public class GaussianQuadrature {
    public static double f(double x) {
        return Math.exp(x);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        int n = 3;
        double[] puntos = {-0.774596669, 0.0, 0.774596669};
        double[] pesos = {0.555555556, 0.888888889, 0.555555556};

        double suma = 0;
        for (int i = 0; i < n; i++) {
            double t = puntos[i];
            double x = ((b - a) * t + (b + a)) / 2;
            suma += pesos[i] * f(x);
        }

        double integral = ((b - a) / 2) * suma;
        System.out.printf("Integral aproximada: %.3f%n", integral);
    }
}
```

### Caso de prueba:

```text
Integral aproximada: 1.718
```
### [<- T4 - Diferenciación e Integración Numérica ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T4%20-%20Diferenciaci%C3%B3n%20e%20Integraci%C3%B3n%20Num%C3%A9rica/Introducci%C3%B3n%20a%20la%20DIferenciai%C3%B3n%20e%20Integraci%C3%B3n%20Num%C3%A9rica.md)
