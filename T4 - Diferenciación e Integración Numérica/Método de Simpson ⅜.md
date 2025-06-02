# Tema 4: Método de Simpson 3/8

# Introducción
A diferencia del método 1/3, esta técnica emplea una aproximación mediante polinomios de tercer grado (cbicos) que permite una ajuste más fino de la curva de la función en ciertos contextos.

La fórmula específica que asigna diferentes pesos a los valores de la función en los extremos y en los puntos intermedios. Aunque no es tan común como el método de Simpson 1/3, resulta muy útil en casos en los que el número de subintervalos no permite aplicar directamente aquel método, o cuando se desea una mejor aproximación en ciertos tramos.

La precisión del método 3/8 es generalmente comparable a la del método 1/3, y puede ser superior en situaciones específicas. Sin embargo, como todos los métodos numéricos, su efectividad depende de la naturaleza de la función a integrar y del tamaño de los subintervalos. En conjunto con otros métodos, ofrece una excelente herramienta para integrar funciones que no pueden resolverse de forma analítica.

---

### Ventajas y Desventajas

**Ventajas:**
- Utiliza polinomios cúbicos, lo que puede mejorar la precisión en ciertas funciones.
- Aplicable cuando el número de subintervalos es múltiplo de tres.
- Ofrece una alternativa útil cuando el método 1/3 no es viable.

**Desventajas:**
- Requiere un número de subintervalos múltiplo de tres, lo que limita su flexibilidad.
- Puede ser menos eficiente que el método 1/3 en términos de implementación.
- Pierde precisión si la función tiene discontinuidades o cambios bruscos.

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
  Definir h como real
  Definir suma como real
  Definir x como real
  Definir i como entero
  Definir integral como real

  a = 0.0
  b = 1.0
  n = 3

  Si n mod 3 != 0
    Imprimir "El número de subintervalos debe ser múltiplo de 3"
    Retornar
  Fin Si

  h = (b - a) / n
  suma = f(a) + f(b)

  Para i = 1 hasta n-1
    x = a + i * h
    Si i mod 3 = 0
      suma = suma + 2 * f(x)
    Sino
      suma = suma + 3 * f(x)
    Fin Si
  Fin Para

  integral = (3 * h / 8) * suma
  Imprimir "Integral aproximada: ", integral
Fin
```

### Código base en Java

```java
public class CodigoBaseSimpsonThreeEighths {
    public static double f(double x) {
        return Math.exp(x);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        int n = 3;

        if (n % 3 != 0) {
            System.out.println("El número de subintervalos debe ser múltiplo de 3");
            return;
        }

        double h = (b - a) / n;
        double suma = f(a) + f(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 3 == 0) {
                suma += 2 * f(x);
            } else {
                suma += 3 * f(x);
            }
        }

        double integral = (3 * h / 8) * suma;
        System.out.println("Integral aproximada: " + integral);
    }
}
```

### Ejemplo funcional en Java

```java
public class SimpsonThreeEighths {
    public static double f(double x) {
        return Math.exp(x);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        int n = 3;

        if (n % 3 != 0) {
            System.out.println("El número de subintervalos debe ser múltiplo de 3");
            return;
        }

        double h = (b - a) / n;
        double suma = f(a) + f(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 3 == 0) {
                suma += 2 * f(x);
            } else {
                suma += 3 * f(x);
            }
        }

        double integral = (3 * h / 8) * suma;
        System.out.printf("Integral aproximada: %.3f%n", integral);
    }
}
```

### Caso de prueba:

```text
Integral aproximada: 1.718
```
### [<- T4 - Diferenciación e Integración Numérica ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ce2d60bd3530bdd5b33752fc08ea9a856a6a37e5/T4%20-%20Diferenciaci%C3%B3n%20e%20Integraci%C3%B3n%20Num%C3%A9rica/Introducci%C3%B3n%20a%20la%20DIferenciai%C3%B3n%20e%20Integraci%C3%B3n%20Num%C3%A9rica.md)
