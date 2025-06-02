# Tema 4: Método del Trapecio

## Introducción 

El método del trapecio es una de las técnicas más simples y ampliamente utilizadas en la integración numérica . Se basa en aproximar el área bajo la curva de una función mediante trapecios , en lugar de rectángulos , y se calcula el área.

Aunque su precisión es menor en comparación con métodos como el de Simpson, su simplicidad y facilidad de implementación lo convierten en una opción válida para muchas aplicaciones prácticas.

El error asociado al método del trapecio depende del tamaño de los subintervalos y de la curvatura de la función. Si la función es lineal o casi lineal, el resultado es muy preciso. 

Sin embargo, si la función tiene una curvatura considerable, es necesario subdividir el intervalo en muchas partes pequeñas para lograr una buena aproximación. Aun así, por su equilibrio entre simplicidad y exactitud, sigue siendo un método muy valorado en el campo del análisis numérico.

---

### Ventajas y Desventajas

**Ventajas:**
- Extremadamente simple de implementar y entender.
- Eficaz para funciones casi lineales o con pocos subintervalos.
- Puede mejorarse fácilmente con el método compuesto.

**Desventajas:**
- Menor precisión que métodos como Simpson para funciones no lineales.
- El error aumenta con la curvatura de la función.
- Requiere más subintervalos para aproximaciones precisas en funciones complejas.

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
  n = 4

  h = (b - a) / n
  suma = f(a) + f(b)

  Para i = 1 hasta n-1
    x = a + i * h
    suma = suma + 2 * f(x)
  Fin Para

  integral = (h / 2) * suma
  Imprimir "Integral aproximada: ", integral
Fin
```

### Código base en Java

```java
public class CodigoBaseTrapezoidalRule {
    public static double f(double x) {
        return Math.exp(x);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        int n = 4;

        double h = (b - a) / n;
        double suma = f(a) + f(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            suma += 2 * f(x);
        }

        double integral = (h / 2) * suma;
        System.out.println("Integral aproximada: " + integral);
    }
}
```

### Ejemplo funcional en Java

```java
public class TrapezoidalRule {
    public static double f(double x) {
        return Math.exp(x);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = 1.0;
        int n = 4;

        double h = (b - a) / n;
        double suma = f(a) + f(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            suma += 2 * f(x);
        }

        double integral = (h / 2) * suma;
        System.out.printf("Integral aproximada: %.3f%n", integral);
    }
}
```

### Caso de prueba:

```text
Integral aproximada: 1.721
```
### [<- T4 - Diferenciación e Integración Numérica ](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/c9829f46be4ec2aa47381fa4eb9504aa16c8d72e/T4/Introducci%C3%B3n%20a%20la%20Diferenciaci%C3%B3n%20e%20Integraci%C3%B3n%20Num%C3%A9rica.md)
