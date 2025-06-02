## Tema 1: Error de Truncamiento

## ¿Que es?

El error de truncamiento se produce cuando se interrumpe o se simplifica una operación matemática infinita o continua para poder ser calculada de forma finita . Por ejemplo, al utilizar una serie de Taylor , es necesario cortar la serie después de un nmero determinado de términos, lo que introduce un error al omiti

idad de términos considerados, menor será el error, pero mayor será el costo computacional. Existe un compromiso entre precisión y eficiencia que debe ser evaluado según el problema específico.

---

### Ventajas y Desventajas

**Ventajas:**
- Permite realizar cálculos aproximados de funciones complejas que serían imposibles de calcular de forma exacta.
- Ofrece un control directo sobre el balance entre precisión y costo computacional al ajustar el número de términos.
- Es útil en aplicaciones prácticas donde una aproximación suficientemente precisa es aceptable.

**Desventajas:**
- Introduce un error inherente que puede acumularse en cálculos posteriores.
- Requiere un análisis cuidadoso para determinar el número adecuado de términos y minimizar el error.
- Puede ser computacionalmente costoso si se necesitan muchos términos para alcanzar la precisión deseada.

---

### Pseudocódigo

```java
Inicio
  Función funciónReal(x)
    Retornar exp(x)
  Fin Función

  Función aproximacionTaylor(x, n)
    Definir suma como real
    Definir i como entero
    suma = 0
    Para i = 0 hasta n
      suma = suma + (x^i) / factorial(i)
    Fin Para
    Retornar suma
  Fin Función

  Definir x como real
  Definir n como entero
  Definir real como real
  Definir aproximado como real
  x = 1.0
  n = 3
  real = funciónReal(x)
  aproximado = aproximacionTaylor(x, n)
  Imprimir "Valor real: ", real
  Imprimir "Aproximación: ", aproximado
  Imprimir "Error de truncamiento: ", abs(real - aproximado)
Fin
```

### Código base en Java

```java
public class CodigoBaseTruncamiento {
    public static double funcionReal(double x) {
        return Math.exp(x);
    }

    public static double aproximacionTaylor(double x, int n) {
        double suma = 0;
        for (int i = 0; i <= n; i++) {
            double factorial = 1;
            for (int j = 1; j <= i; j++) {
                factorial *= j;
            }
            suma += Math.pow(x, i) / factorial;
        }
        return suma;
    }

    public static void main(String[] args) {
        double x = 1.0;
        int n = 3;
        double real = funcionReal(x);
        double aproximado = aproximacionTaylor(x, n);

        System.out.println("Valor real: " + real);
        System.out.println("Aproximación: " + aproximado);
        System.out.println("Error de truncamiento: " + Math.abs(real - aproximado));
    }
}
```

### Ejemplo funcional en Java

```java
public class ErrorTruncamiento {
    public static double taylorExp(double x, int n) {
        double suma = 1.0;
        double term = 1.0;

        for (int i = 1; i <= n; i++) {
            term *= x / i;
            suma += term;
        }

        return suma;
    }

    public static void main(String[] args) {
        double x = 1.0;
        int n = 3;
        double real = Math.exp(x);
        double aproximado = taylorExp(x, n);

        System.out.printf("Valor real: %.3f%n", real);
        System.out.printf("Aproximación (n=3): %.3f%n", aproximado);
        System.out.printf("Error de truncamiento: %.3f%n", Math.abs(real - aproximado));
    }
}
```

### Caso de prueba:

```text
Valor real: 2.718
Aproximación (n=3): 2.667
Error de truncamiento: 0.051
```
### [<- Regresar a T1 - Introducción a los Métodos Numéricos](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ae1f13f7ca5adf0391f0615d7c2a904a1cbd981c/T1/Introducci%C3%B3n%20a%20los%20Metodos%20Numericos.md)
