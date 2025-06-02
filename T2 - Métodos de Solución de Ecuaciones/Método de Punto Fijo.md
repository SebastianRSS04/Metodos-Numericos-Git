# Tema 2: Método de Punto Fijo

## Introducción 
El método de punto fijo es una estrategia numérica consisting en reformular una ecuación en una nueva expresión donde la incógnita aparece de forma explcita como función de s misma . Si se logra este objetivo, se dice que se ha encontrado un punto fijo, lo que lo hace accesible para una amplia variedad de funciones. Sin embargo, su éxito depende en gran medida de cómo se transforme la ecuación original. No cualquier reformulación asegura que el proceso converja, por lo que se debe tener precaución al plantear la función que se utilizará.

La convergencia del método de punto fijo puede ser lenta y, en algunos casos, no garantiza llegar a una solución. Por ello, se recomienda usarlo cuando se tiene una buena comprensión de la función y cuando es posible verificar que las condiciones necesarias para la convergencia se cumplen. A pesar de sus limitaciones, sigue siendo una opción válida en ciertos escenarios.

---

### Ventajas y Desventajas

**Ventajas:**
- No requiere calcular derivadas, lo que lo hace más simple que métodos como Newton-Raphson.
- Es intuitivo y fácil de implementar para funciones bien reformuladas.
- Puede ser útil en problemas donde otras técnicas no son aplicables debido a la falta de derivadas.

**Desventajas:**
- La convergencia no está garantizada y depende de la reformulación de la ecuación y del punto inicial.
- Puede converger lentamente en comparación con otros métodos numéricos.
- Requiere un análisis previo para asegurar que la función cumpla las condiciones de convergencia (como que la derivada de g(x) tenga magnitud menor a 1).

---

### Pseudocódigo

```text
Inicio
  Función f(x)
    Retornar x^3 - x - 2
  Fin Función

  Función g(x)
    Retornar (x + 2)^(1/3)
  Fin Función

  Definir x como real
  Definir tolerancia como real
  Definir maxIteraciones como entero
  Definir iteracion como entero
  Definir xNuevo como real

  x = 1.5
  tolerancia = 0.001
  maxIteraciones = 100
  iteracion = 0

  Mientras iteracion < maxIteraciones
    xNuevo = g(x)
    Imprimir "Iteración ", iteracion, ": x = ", xNuevo, ", f(x) = ", f(xNuevo)

    Si abs(xNuevo - x) < tolerancia
      Imprimir "Raíz encontrada: ", xNuevo
      Retornar
    Fin Si

    x = xNuevo
    iteracion = iteracion + 1
  Fin Mientras

  Imprimir "Máximo de iteraciones alcanzado"
Fin
```

### Código base en Java

```java
public class CodigoBasePuntoFijo {
    public static double f(double x) {
        return Math.pow(x, 3) - x - 2;
    }

    public static double g(double x) {
        return Math.pow(x + 2, 1.0 / 3.0);
    }

    public static void main(String[] args) {
        double x = 1.5;
        double tolerancia = 0.001;
        int maxIteraciones = 100;
        int iteracion = 0;

        while (iteracion < maxIteraciones) {
            double xNuevo = g(x);
            System.out.println("Iteración " + iteracion + ": x = " + xNuevo + ", f(x) = " + f(xNuevo));

            if (Math.abs(xNuevo - x) < tolerancia) {
                System.out.println("Raíz encontrada: " + xNuevo);
                return;
            }

            x = xNuevo;
            iteracion++;
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Ejemplo funcional en Java

```java
public class FixedPointMethod {
    public static double f(double x) {
        return x * x * x - x - 2;
    }

    public static double g(double x) {
        return Math.pow(x + 2, 1.0 / 3.0);
    }

    public static void main(String[] args) {
        double x = 1.5;
        double tolerancia = 0.001;
        int maxIteraciones = 100;

        for (int iteracion = 0; iteracion < maxIteraciones; iteracion++) {
            double xNuevo = g(x);
            System.out.printf("Iteración %d: x = %.3f, f(x) = %.3f%n", iteracion, xNuevo, f(xNuevo));

            if (Math.abs(xNuevo - x) < tolerancia) {
                System.out.printf("Raíz encontrada: %.3f%n", xNuevo);
                return;
            }

            x = xNuevo;
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Caso de prueba:

```text
Iteración 0: x = 1.442, f(x) = 0.150
Iteración 1: x = 1.567, f(x) = 0.321
Iteración 2: x = 1.484, f(x) = 0.075
Iteración 3: x = 1.533, f(x) = 0.069
Iteración 4: x = 1.506, f(x) = 0.029
Iteración 5: x = 1.522, f(x) = 0.016
Iteración 6: x = 1.514, f(x) = 0.006
Iteración 7: x = 1.518, f(x) = 0.003
Iteración 8: x = 1.520, f(x) = 0.001
Raíz encontrada: 1.520
```
### [<- Regresar a T2 - Métodos de Solución de Ecuaciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T2/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones.md)
