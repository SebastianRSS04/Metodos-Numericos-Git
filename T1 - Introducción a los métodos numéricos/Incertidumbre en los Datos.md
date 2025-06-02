## Tema 1: Incertidumbre en los Datos

# Qué es?  

En muchos problemas reales, los datos de entrada no se conocen con exactitud absoluta. Esta incertidumbre puede deberse a limitaciones en la medición, ruido experimental, redondeo de valores o estimaciones subjetivas problema es sensible a pequeñas variaciones en los datos (mal condicionado). Por ello, se recomienda realizar análisis de sensibilidad y estimaciones de error para comprender su impacto.

---

### Ventajas y Desventajas

**Ventajas:**
- Permite modelar y analizar problemas reales donde los datos son intrínsecamente imprecisos.
- Facilita la evaluación de rangos de resultados posibles mediante análisis de sensibilidad.
- Ayuda a tomar decisiones informadas al considerar la incertidumbre en los datos.

**Desventajas:**
- Introduce incertidumbre en los resultados, lo que puede dificultar la interpretación exacta.
- Requiere métodos adicionales para estimar y controlar el impacto de los errores.
- Puede aumentar la complejidad computacional al realizar múltiples cálculos para diferentes escenarios.

---

### Pseudocódigo

```java
Inicio
  Definir medicionOriginal como real
  Definir errorSensor como real
  Definir minimo como real
  Definir maximo como real
  medicionOriginal = 9.81
  errorSensor = 0.05
  minimo = medicionOriginal - errorSensor
  maximo = medicionOriginal + errorSensor
  Imprimir "Medición original: ", medicionOriginal
  Imprimir "Rango con incertidumbre: [", minimo, ", ", maximo, "]"
Fin
```

### Código base en Java

```java
public class CodigoBaseIncertidumbre {
    public static void main(String[] args) {
        double medicionOriginal = 9.81;
        double errorSensor = 0.05;
        double minimo = medicionOriginal - errorSensor;
        double maximo = medicionOriginal + errorSensor;

        System.out.println("Medición original: " + medicionOriginal);
        System.out.println("Rango con incertidumbre: [" + minimo + ", " + maximo + "]");
    }
}
```

### Ejemplo funcional en Java

```java
public class IncertidumbreDatos {
    public static void main(String[] args) {
        double valorMedido = 100.0;
        double margenError = 2.5;
        double minimo = valorMedido - margenError;
        double maximo = valorMedido + margenError;

        System.out.printf("Valor medido: %.3f%n", valorMedido);
        System.out.printf("Rango estimado: [%.3f, %.3f]%n", minimo, maximo);
        System.out.printf("Incertidumbre en los datos: ±%.3f%n", margenError);
    }
}
```

### Caso de prueba:

```java
Valor medido: 100.000
Rango estimado: [97.500, 102.500]
Incertidumbre en los datos: ±2.500
```
### [<- Regresar a T1 - Introducción a los Métodos Numéricos](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ae1f13f7ca5adf0391f0615d7c2a904a1cbd981c/T1/Introducci%C3%B3n%20a%20los%20Metodos%20Numericos.md)
