# Tema 2: Método de la Regla Falsa

## Introducción 

El método de la regla falsa , también conocido como método de falsa posición , es una técnica que combina la seguridad del método de bisección con un enfoque más eficiente para aproximar races . En lugar de dividir el intervalo en dos que puede ser más rápido que la bisección, ya que la estimación está basada en el comportamiento de la función, no solo en una división arbitraria. Sin embargo, puede presentar un problema si uno de los extremos se mantiene fijo durante varias iteraciones, lo que reduce la eficiencia del proceso.

Este método es especialmente útil cuando se requiere un equilibrio entre precisión y velocidad, sin la necesidad de utilizar derivadas. Es considerado una mejora del método de bisección y resulta adecuado para muchas aplicaciones prácticas, especialmente cuando se conocen los signos de la función en los extremos del intervalo.

---

### Ventajas y Desventajas

**Ventajas:**
- Convierge más rápido que el método de bisección al utilizar la pendiente de la función.
- Garantiza convergencia si hay un cambio de signo en el intervalo y la función es continua.
- No requiere cálculos de derivadas, lo que lo hace más simple que métodos como Newton-Raphson.

**Desventajas:**
- Puede volverse ineficiente si un extremo se mantiene fijo durante varias iteraciones.
- La velocidad de convergencia puede variar dependiendo de la forma de la función.
- Requiere un intervalo inicial que contenga la raíz, similar a la bisección.

---

### Pseudocódigo

```text
Inicio
  Función f(x)
    Retornar x^3 - x - 2
  Fin Función

  Definir a como real
  Definir b como real
  Definir tolerancia como real
  Definir maxIteraciones como entero
  Definir iteracion como entero
  Definir p como real
  Definir fa como real
  Definir fb como real
  Definir fp como real

  a = 1.0
  b = 2.0
  tolerancia = 0.001
  maxIteraciones = 100
  iteracion = 0

  fa = f(a)
  fb = f(b)

  Si fa * fb >= 0
    Imprimir "El intervalo no contiene una raíz"
    Retornar
  Fin Si

  Mientras iteracion < maxIteraciones
    p = a - (fa * (b - a)) / (fb - fa)
    fp = f(p)
    Imprimir "Iteración ", iteracion, ": x = ", p, ", f(x) = ", fp

    Si abs(fp) < tolerancia
      Imprimir "Raíz encontrada: ", p
      Retornar
    Fin Si

    Si fa * fp < 0
      b = p
      fb = fp
    Sino
      a = p
      fa = fp
    Fin Si

    iteracion = iteracion + 1
  Fin Mientras

  Imprimir "Máximo de iteraciones alcanzado"
Fin
```

### Código base en Java

```java
public class CodigoBaseReglaFalsa {
    public static double f(double x) {
        return Math.pow(x, 3) - x - 2;
    }

    public static void main(String[] args) {
        double a = 1.0;
        double b = 2.0;
        double tolerancia = 0.001;
        int maxIteraciones = 100;
        int iteracion = 0;

        double fa = f(a);
        double fb = f(b);

        if (fa * fb >= 0) {
            System.out.println("El intervalo no contiene una raíz");
            return;
        }

        while (iteracion < maxIteraciones) {
            double p = a - (fa * (b - a)) / (fb - fa);
            double fp = f(p);
            System.out.println("Iteración " + iteracion + ": x = " + p + ", f(x) = " + fp);

            if (Math.abs(fp) < tolerancia) {
                System.out.println("Raíz encontrada: " + p);
                return;
            }

            if (fa * fp < 0) {
                b = p;
                fb = fp;
            } else {
                a = p;
                fa = fp;
            }

            iteracion++;
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Ejemplo funcional en Java

```java
public class FalsePositionMethod {
    public static double f(double x) {
        return x * x * x - x - 2;
    }

    public static void main(String[] args) {
        double a = 1.0;
        double b = 2.0;
        double tolerancia = 0.001;
        int maxIteraciones = 100;

        double fa = f(a);
        double fb = f(b);

        if (fa * fb >= 0) {
            System.out.println("El intervalo no contiene una raíz");
            return;
        }

        for (int iteracion = 0; iteracion < maxIteraciones; iteracion++) {
            double p = a - (fa * (b - a)) / (fb - fa);
            double fp = f(p);
            System.out.printf("Iteración %d: x = %.3f, f(x) = %.3f%n", iteracion, p, fp);

            if (Math.abs(fp) < tolerancia) {
                System.out.printf("Raíz encontrada: %.3f%n", p);
                return;
            }

            if (fa * fp < 0) {
                b = p;
                fb = fp;
            } else {
                a = p;
                fa = fp;
            }
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Caso de prueba:

```text
Iteración 0: x = 1.556, f(x) = 0.214
Iteración 1: x = 1.518, f(x) = 0.002
Raíz encontrada: 1.518
```
### [<- Regresar a T2 - Métodos de Solución de Ecuaciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/660d16f952064f0ad7c71e139136c1df3cc575f3/T2%20-%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones.md)
