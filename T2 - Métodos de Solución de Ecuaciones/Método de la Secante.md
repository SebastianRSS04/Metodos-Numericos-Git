# Tema 2: Método de la Secante

## Introducción 
El método de la secante es una técnica iterativa para encontrar races busca mejorar la eficiencia del método of Newton-Raphson, eliminando la necesidad de calcular derivadas. A partir de dos valores iniciales, se genera una aproximación de la raz, que métodos como la bisección y más práctico que Newton-Raphson cuando no se dispone de la derivada de la función. Sin embargo, es menos estable y puede divergir si los valores iniciales no están bien escogidos o si la función es muy irregular o no cumple ciertas condiciones.

El método de la secante es muy útil en situaciones donde la derivada es difícil de calcular o simplemente no está disponible. Aunque no siempre garantiza la convergencia, su simplicidad y eficiencia lo convierten en una opción atractiva en problemas reales donde se busca una solución rápida con bajo costo computacional.

---

### Ventajas y Desventajas

**Ventajas:**
- No requiere calcular derivadas, lo que lo hace más práctico que el método de Newton-Raphson.
- Converge más rápido que el método de bisección en muchos casos.
- Es simple de implementar y eficiente para funciones bien comportadas.

**Desventajas:**
- La convergencia no está garantizada y puede divergir si los valores iniciales no son adecuados.
- Es menos estable que métodos como la bisección o la regla falsa, especialmente en funciones irregulares.
- Puede ser sensible a la elección de los puntos iniciales y a la forma de la función.

---

### Pseudocódigo

```text
Inicio
  Función f(x)
    Retornar x^3 - x - 2
  Fin Función

  Definir x0 como real
  Definir x1 como real
  Definir tolerancia como real
  Definir maxIteraciones como entero
  Definir iteracion como entero
  Definir x2 como real
  Definir fx0 como real
  Definir fx1 como real

  x0 = 1.0
  x1 = 2.0
  tolerancia = 0.001
  maxIteraciones = 100
  iteracion = 0

  Mientras iteracion < maxIteraciones
    fx0 = f(x0)
    fx1 = f(x1)
    x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
    Imprimir "Iteración ", iteracion, ": x = ", x2, ", f(x) = ", f(x2)

    Si abs(f(x2)) < tolerancia
      Imprimir "Raíz encontrada: ", x2
      Retornar
    Fin Si

    x0 = x1
    x1 = x2
    iteracion = iteracion + 1
  Fin Mientras

  Imprimir "Máximo de iteraciones alcanzado"
Fin
```

### Código base en Java

```java
public class CodigoBaseSecante {
    public static double f(double x) {
        return Math.pow(x, 3) - x - 2;
    }

    public static void main(String[] args) {
        double x0 = 1.0;
        double x1 = 2.0;
        double tolerancia = 0.001;
        int maxIteraciones = 100;
        int iteracion = 0;

        while (iteracion < maxIteraciones) {
            double fx0 = f(x0);
            double fx1 = f(x1);
            double x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0);
            System.out.println("Iteración " + iteracion + ": x = " + x2 + ", f(x) = " + f(x2));

            if (Math.abs(f(x2)) < tolerancia) {
                System.out.println("Raíz encontrada: " + x2);
                return;
            }

            x0 = x1;
            x1 = x2;
            iteracion++;
        }
        System.out.println("Máximo de iteraciones alcanzado");
    }
}
```

### Ejemplo funcional en Java

```java
public class SecantMethod {
    public static double f(double x) {
        return x * x * x - x - 2;
    }

    public static void main(String[] args) {
        double x0 = 1.0;
        double x1 = 2.0;
        double tolerancia = 0.001;
        int maxIteraciones = 100;

        for (int iteracion = 0; iteracion < maxIteraciones; iteracion++) {
            double fx0 = f(x0);
            double fx1 = f(x1);
            double x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0);
            System.out.printf("Iteración %d: x = %.3f, f(x) = %.3f%n", iteracion, x2, f(x2));

            if (Math.abs(f(x2)) < tolerancia) {
                System.out.printf("Raíz encontrada: %.3f%n", x2);
                return;
            }

            x0 = x1;
            x1 = x2;
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
### [<- Regresar a T2 - Métodos de Solución de Ecuaciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T2/Introducci%C3%B3n%20a%20los%20M%C3%A9todos%20de%20Soluci%C3%B3n%20de%20Ecuaciones.md)
