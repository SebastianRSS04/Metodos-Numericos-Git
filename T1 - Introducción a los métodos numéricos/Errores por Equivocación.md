## Tema 1: Errores por Equivocación

# Qué es? 

Los errores por equivocación, conocidos como errores humanos, ocurren cuando se comete una falla durante la formulación, programación o ejecución de un método numérico . Estos pueden incluir errores al ingresar datos, seleccionar mal el método para

ritmos incluye la validación de resultados, revisión cruzada de código y verificación de entradas y salidas para minimizar estos errores.

---

### Ventajas y Desventajas

**Ventajas:**
- Identificar estos errores fomenta mejores prácticas de programación, como la validación y verificación de datos.
- Puede prevenir problemas mayores mediante revisiones y pruebas rigurosas.
- Ayuda a mejorar la calidad general del código y los resultados al implementar controles de calidad.

**Desventajas:**
- Son impredecibles y dependen del factor humano, lo que los hace difíciles de evitar completamente.
- Pueden requerir tiempo adicional para depuración y corrección.
- Su impacto puede ser significativo, incluso en sistemas bien diseñados, si no se detectan a tiempo.

---

### Pseudocódigo

```java
Inicio
  Definir areaCorrecta como real
  Definir areaConError como real
  areaCorrecta = π * (5^2)
  areaConError = π * (10^2)
  Imprimir "Área correcta: ", areaCorrecta
  Imprimir "Área con error: ", areaConError
  Imprimir "Diferencia por equivocación: ", abs(areaCorrecta - areaConError)
Fin
```

### Código base en Java

```java
public class CodigoBaseEquivocacion {
    public static void main(String[] args) {
        double areaCorrecta = Math.PI * Math.pow(5, 2);
        double areaConError = Math.PI * Math.pow(10, 2);

        System.out.println("Área correcta: " + areaCorrecta);
        System.out.println("Área con error: " + areaConError);
        System.out.println("Diferencia por equivocación: " + Math.abs(areaCorrecta - areaConError));
    }
}
```

### Ejemplo funcional en Java

```java
public class ErrorEquivocacion {
    public static void main(String[] args) {
        double radio = 5.0;
        double areaIncorrecta = Math.PI * radio * 2;
        double areaCorrecta = Math.PI * Math.pow(radio, 2);
        double diferencia = Math.abs(areaCorrecta - areaIncorrecta);

        System.out.printf("Área incorrecta: %.3f%n", areaIncorrecta);
        System.out.printf("Área correcta: %.3f%n", areaCorrecta);
        System.out.printf("Diferencia por equivocación: %.3f%n", diferencia);
    }
}
```

### Caso de prueba:

```java
Área incorrecta: 31.416
Área correcta: 78.540
Diferencia por equivocación: 47.124
```
### [<- Regresar a T1 - Introducción a los Métodos Numéricos](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ae1f13f7ca5adf0391f0615d7c2a904a1cbd981c/T1/Introducci%C3%B3n%20a%20los%20Metodos%20Numericos.md)
