## Tema 1: Errores de Formulación

Los errores de formulación se produce cuando el modelo matemático used to describir un problema real es incorrecto o incompleto . Muchas veces se hacen simplificaciones o suposiciones que alejan el modelo de la realidad . Estos errores son especialmente peligrosos porque pueden pasar desapercibidos si el model

 modelo parece funcionar correctamente bajo ciertas condiciones. Una formulación incorrecta puede invalidar completamente los resultados, sin importar qué tan preciso sea el método empleado.

---

### Ventajas y Desventajas 

**Ventajas:**
- Permite resolver problemas complejos mediante simplificaciones que hacen los cálculos manejables.
- Reduce el tiempo y los recursos computacionales necesarios para modelar fenómenos.
- Facilita la comprensión y comunicación de conceptos al abstraer detalles secundarios.

**Desventajas:**
- Las simplificaciones pueden introducir errores significativos que afectan la validez de los resultados.
- Puede ser difícil detectar si el modelo es inadecuado sin pruebas extensivas contra datos reales.
- Los resultados pueden ser engañosos si las suposiciones del modelo no se verifican adecuadamente.

---

### Pseudocódigo

```java
Inicio
  Definir g como real
  Definir t como real
  Definir distanciaIdeal como real
  g = 9.81
  t = 3.0
  distanciaIdeal = 0.5 * g * t^2
  Imprimir "Distancia sin resistencia del aire: ", distanciaIdeal
  Imprimir "Nota: Se desprecia la resistencia del aire (modelo simplificado)"
Fin
```
### Código base en Java

```java
public class CodigoBaseFormulacion {
    public static void main(String[] args) {
        double g = 9.81;
        double t = 3.0;
        double distanciaIdeal = 0.5 * g * t * t;

        System.out.println("Distancia sin resistencia del aire: " + distanciaIdeal);
        System.out.println("Nota: Se desprecia la resistencia del aire (modelo simplificado)");
    }
}
```
### Ejemplo funcional en Java

```java
public class ErrorFormulacion {
    public static void main(String[] args) {
        double g = 9.81;
        double tiempo = 3.0;
        double distanciaIdeal = 0.5 * g * Math.pow(tiempo, 2);
        double distanciaEsperada = 44.145; // Valor teórico para comparación

        System.out.printf("Distancia calculada (modelo ideal): %.3f metros%n", distanciaIdeal);
        System.out.printf("Distancia esperada: %.3f metros%n", distanciaEsperada);
        System.out.println("Error por formulación: " + Math.abs(distanciaEsperada - distanciaIdeal));
        System.out.println("Nota: No se considera resistencia del aire.");
    }
}
```

# Caso de prueba:

```java
Distancia calculada (modelo ideal): 44.145 metros
Distancia esperada: 44.145 metros
Error por formulación: 0.0
Nota: No se considera resistencia del aire.
```
### [<- Regresar a T1 - Introducción a los Métodos Numéricos](https://github.com/Yayackie/Trabajos_Metodos-Numericos/blob/main/T1%20-%20Introducci%C3%B3n%20a%20los%20m%C3%A9todos%20num%C3%A9ricos/Introducci%C3%B3n%20a%20los%20m%C3%A9todos%20n%C3%BAmericos.md)
