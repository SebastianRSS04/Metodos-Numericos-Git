# Tema 2: Método de Newton-Raphson

## Introducción 

El método de Newton-Raphson es uno de los más utilizados para encontrar races de funciones debido a su velocidad y eficiencia . A partir de una suposición inicial cercana a la solución, el método mejora progresivamente dicha aproximación utilizando información sea derivable, ya que el proceso se basa en analizar la pendiente de la función en cada paso. Si la derivada es cero o muy pequeña cerca del valor buscado, el método puede fallar o divergir, lo que lo hace sensible a la elección del punto de inicio.

A pesar de estas limitaciones, cuando se utiliza correctamente, el método de Newton-Raphson destaca por su rapidez en comparación con otros métodos. Es especialmente útil en funciones suaves y bien definidas, y se convierte en una herramienta poderosa para problemas en ingeniería, ciencias aplicadas y matemáticas computacionales.

---

### Ventajas y Desventajas

**Ventajas:**
- Converge rápidamente (con orden cuadrático) si la suposición inicial es buena y la función es bien comportada.
- Requiere menos iteraciones que métodos como la bisección para alcanzar la misma precisión.
- Es ideal para funciones suaves y derivables, comunes en aplicaciones prácticas.

**Desventajas:**
- Sensible a la elección del punto inicial; una mala elección puede llevar a divergencia.
- Requiere calcular la derivada de la función, lo que puede ser complicado o costoso computacionalmente.
- Puede fallar si la derivada es cero o muy pequeña cerca de la raíz, o si la función tiene discontinuidades.

---

### Pseudocódigo

```text
Inicio
  Función f(x)
    Retornar x^3 - x - 2
  Fin Función

  Función fPrima(x)
    Retornar 3 * x^2 - 1
  Fin Función

  Definir x como real
  Definir tolerancia como real
  Definir maxIteraciones como entero
  Definir iteracion como entero
  Definir fx como real

  x = 1.5
  tolerancia = 0.001
  maxIteraciones = 100
  iteracion = 0

  Mientras iteracion < maxIteraciones
    fx = f(x)
    Imprimir "Iteración ", iteracion, ": x = ", x, ", f(x) = ", fx

    Si abs(fx) < tolerancia
      Imprimir "Raíz encontrada: ", x
      Retornar
    Fin Si

    x = x - fx / fPrima(x)
    iteracion = iteracion + 1
  Fin Mientras

  Imprimir "Máximo de iteraciones alcanzado"
Fin
```

### Código base en Java

```java
public class CodigoBaseNewtonRaphson {
    public static double f(double x) {
        return Math.pow(x, 3) - x - 2;
    }

    public static double fPrima(double x) {
        return 3 * Math.pow(x, 2) - 1;
    }

    public static void main(String[] args) {
        double x = 1.5;
        double tolerancia = 0.001;
        int maxIteraciones = 100;
        int iteracion = 0;

        while (iteracion < maxIteraciones) {
            double fx = f(x);
            System.out.println("Iteración " + iteracion + ": x = " + x + ", f(x) = " + fx);

            if (Math.abs(fx) < tolerancia) {
                System.out.println("Raíz encontrada: " + x);
                return;
            }

            x = x - fx / fPrima(x);
            iteracion++;
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Ejemplo funcional en Java

```java
public class NewtonRaphsonMethod {
    public static double f(double x) {
        return x * x * x - x - 2;
    }

    public static double fPrima(double x) {
        return 3 * x * x - 1;
    }

    public static void main(String[] args) {
        double x = 1.5;
        double tolerancia = 0.001;
        int maxIteraciones = 100;

        for (int iteracion = 0; iteracion < maxIteraciones; iteracion++) {
            double fx = f(x);
            System.out.printf("Iteración %d: x = %.3f, f(x) = %.3f%n", iteracion, x, fx);

            if (Math.abs(fx) < tolerancia) {
                System.out.printf("Raíz encontrada: %.3f%n", x);
                return;
            }

            x = x - fx / fPrima(x);
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Caso de prueba:

```text
Iteración 0: x = 1.500, f(x) = -0.125
Iteración 1: x = 1.521, f(x) = 0.001
Raíz encontrada: 1.521
```
### [<- Regresar a T2 - Métodos de Solución de Ecuaciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/660d16f952064f0ad7c71e139136c1df3cc575f3/T2%20-%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones.md)
