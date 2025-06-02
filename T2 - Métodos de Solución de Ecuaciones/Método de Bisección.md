# Tema 2: Método de Bisección

## Introducción 

El método de bisección es una técnica clásica used to encontrar soluciones aproximadas a ecuaciones cuando no se puede obtener la raz de forma exacta . Este método se basa en dividir un intervalo en dos partes iguales, observando en cu

ad y la certeza de convergencia, siempre que la función sea continua en el intervalo y que exista un cambio de signo entre los extremos del mismo. Debido a esto, el método de bisección es considerado uno de los más seguros, aunque no es el más eficiente en términos de velocidad de aproximación.

Este método no requiere el conocimiento de derivadas ni características complejas de la función, por lo que es ideal para introducirse en el estudio de los métodos numéricos. A pesar de su lentitud, su confiabilidad lo convierte en una herramienta muy valiosa para asegurar soluciones iniciales que pueden ser refinadas luego por otros métodos más rápidos.

---

### Ventajas y Desventajas

**Ventajas:**
- Garantiza convergencia si se cumple la condición de cambio de signo y la función es continua.
- Es simple de implementar y no requiere conocimientos avanzados de la función (como derivadas).
- Proporciona un método robusto para encontrar raíces iniciales que pueden refinarse con otros métodos.

**Desventajas:**
- Converge más lentamente en comparación con otros métodos numéricos, como Newton-Raphson.
- Requiere un intervalo inicial que contenga la raíz, lo que puede ser difícil de determinar.
- No es eficiente para funciones con múltiples raíces cercanas, ya que solo encuentra una raíz a la vez.

---

### Pseudocódigo

```java
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
    p = (a + b) / 2
    fp = f(p)
    Imprimir "Iteración ", iteracion, ": x = ", p, ", f(x) = ", fp

    Si abs(fp) < tolerancia O abs(b - a) < tolerancia
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
public class CodigoBaseBiseccion {
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
            double p = (a + b) / 2;
            double fp = f(p);
            System.out.println("Iteración " + iteracion + ": x = " + p + ", f(x) = " + fp);

            if (Math.abs(fp) < tolerancia || Math.abs(b - a) < tolerancia) {
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
public class BisectionMethod {
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
            double p = (a + b) / 2;
            double fp = f(p);
            System.out.printf("Iteración %d: x = %.3f, f(x) = %.3f%n", iteracion, p, fp);

            if (Math.abs(fp) < tolerancia || Math.abs(b - a) < tolerancia) {
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

```java
Iteración 0: x = 1.500, f(x) = -0.125
Iteración 1: x = 1.750, f(x) = 1.859
Iteración 2: x = 1.625, f(x) = 0.701
Iteración 3: x = 1.563, f(x) = 0.256
Iteración 4: x = 1.531, f(x) = 0.059
Iteración 5: x = 1.516, f(x) = -0.034
Iteración 6: x = 1.523, f(x) = 0.012
Iteración 7: x = 1.520, f(x) = -0.011
Iteración 8: x = 1.522, f(x) = 0.000
Raíz encontrada: 1.522
```

### [<- Regresar a T2 - Métodos de Solución de Ecuaciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T2/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones.md)
