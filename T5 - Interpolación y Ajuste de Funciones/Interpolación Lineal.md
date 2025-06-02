# Tema: Interpolación Lineal 

## Introducción La interpolación lineal 

Es uno de los métodos más simples y directos para estimar el valor de una función entre dos puntos conocidos. Su fundamento es trazar una recta que una dos puntos adyacentes de un conjunto de datos y utilizar la ecución 

Es muy útil cuando se cuenta con pocos datos y se necesita una solución rápida y suficientemente precisa para un intervalo pequeño. Aunque su simplicidad lo hace accesible, también implica una limitación importante: la precisión puede disminuir significativamente si la función real cambia de forma no lineal entre los puntos, lo que genera errores de estimación.

A pesar de su sencillez, la interpolación lineal se utiliza ampliamente en aplicaciones de ingeniería y ciencias aplicadas, especialmente como paso preliminar antes de aplicar métodos más complejos. También sirve como base para entender métodos de interpolación más avanzados, como la interpolación polinómica o spline.

---

### Ventajas y Desventajas

**Ventajas:**
- Muy simple de implementar y computacionalmente eficiente.
- Útil para datos con comportamiento aproximadamente lineal o intervalos pequeños.
- Sirve como base para métodos de interpolación más avanzados.

**Desventajas:**
- Pierde precisión si la función tiene un comportamiento no lineal.
- No es adecuado para intervalos grandes o funciones con cambios bruscos.
- Puede introducir errores significativos si los datos no son representativos.

---

### Pseudocódigo

```text
Inicio
  Definir x como vector de reales [n]
  Definir y como vector de reales [n]
  Definir xp como real
  Definir yp como real
  Definir i como entero

  x = [0, 1, 2, 3]
  y = [1, 2.718, 7.389, 20.085]
  xp = 1.5
  n = 4

  Para i = 0 hasta n-2
    Si x[i] <= xp Y xp <= x[i+1]
      yp = y[i] + (y[i+1] - y[i]) * (xp - x[i]) / (x[i+1] - x[i])
      Imprimir "Valor interpolado en x = ", xp, ": ", yp
      Retornar
    Fin Si
  Fin Para

  Imprimir "Punto fuera del rango de interpolación"
Fin
```

---

### Código base en Java

```java
public class CodigoBaseLinearInterpolation {
    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};
        double xp = 1.5;
        int n = x.length;

        for (int i = 0; i < n - 1; i++) {
            if (x[i] <= xp && xp <= x[i + 1]) {
                double yp = y[i] + (y[i + 1] - y[i]) * (xp - x[i]) / (x[i + 1] - x[i]);
                System.out.println("Valor interpolado en x = " + xp + ": " + yp);
                return;
            }
        }
        System.out.println("Punto fuera del rango de interpolación");
    }
}
```

---

### Ejemplo funcional en Java

```java
public class LinearInterpolation {
    public static double interpolate(double[] x, double[] y, double xp) {
        if (x == null || y == null || x.length != y.length || x.length < 2) {
            throw new IllegalArgumentException("Los vectores x e y deben tener la misma longitud y al menos 2 elementos");
        }
        for (int i = 1; i < x.length; i++) {
            if (x[i] <= x[i - 1]) {
                throw new IllegalArgumentException("El vector x debe estar ordenado en orden ascendente");
            }
        }
        for (int i = 0; i < x.length - 1; i++) {
            if (x[i] <= xp && xp <= x[i + 1]) {
                double yp = y[i] + (y[i + 1] - y[i]) * (xp - x[i]) / (x[i + 1] - x[i]);
                return yp;
            }
        }
        throw new IllegalArgumentException("El punto xp está fuera del rango de interpolación");
    }

    public static void main(String[] args) {
        double[] x = {0, 1, 2, 3};
        double[] y = {1, 2.718, 7.389, 20.085};
        double xp = 1.5;

        try {
            double yp = interpolate(x, y, xp);
            System.out.printf("Interpolación lineal:%n");
            System.out.printf("Punto interpolado: x = %.1f, y = %.3f%n", xp, yp);
            System.out.printf("Puntos usados: (%.1f, %.3f), (%.1f, %.3f)%n", x[1], y[1], x[2], y[2]);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

---

### Caso de prueba:

```text
Interpolación lineal:
Punto interpolado: x = 1.5, y = 5.054
Puntos usados: (1.0, 2.718), (2.0, 7.389)
```
### [<- T5 - Interpolación y Ajuste de Funciones ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T5/Introducci%C3%B3n%20a%20la%20Interpolaci%C3%B3n%20y%20Ajuste%20de%20Funciones.md)
