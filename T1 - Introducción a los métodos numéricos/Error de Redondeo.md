## Tema 1: Tipos de Errores Numéricos

## Tipos de Errores Numéricos

El error de redondeo es uno de los errores más comunes en los métodos numéricos y se origina en la representación limitada de los numeros reales dentro de un sistema digital . Las computadoras utilizan un numero finito de bits para representar numeros y deben redondearse al numero real y su representación computacional.

Aunque un solo error de redondeo puede parecer insignificante, su efecto se vuelve crítico cuando se realizan muchas operaciones aritméticas consecutivas. Las sumas, multiplicaciones, divisiones o funciones más complejas pueden propagar y amplificar estos errores, afectando la precisión final. Por esta razón, es esencial diseñar algoritmos estables que minimicen su acumulación.

---

### Ventajas y Desventajas del Redondeo

**Ventajas:**
- Permite representar números reales en sistemas con recursos limitados.
- Facilita operaciones aritméticas más rápidas al reducir la cantidad de datos que deben procesarse.
- Es necesario para limitar el almacenamiento y mantener la eficiencia computacional.

**Desventajas:**
- Introduce errores que pueden acumularse en cálculos repetitivos o sensibles.
- Puede provocar inestabilidad numérica en algunos algoritmos si no se controla adecuadamente.
- Dificulta la obtención de resultados exactos en ciertas aplicaciones científicas y de ingeniería.

---

## Desarrollo

### Pseudocódigo

```text
Inicio
  Definir a como real
  Definir b como real
  a = 1.0 / 3.0
  b = a * 3.0
  Imprimir "Resultado teórico: 1.0"
  Imprimir "Resultado real: ", b
  Imprimir "Error de redondeo: ", (1.0 - b)
Fin
```

---

### Código base en Java

```java
public class CodigoBaseRedondeo {
    public static void main(String[] args) {
        double a = 1.0 / 3.0;
        double b = a * 3.0;

        System.out.println("Resultado teórico: 1.0");
        System.out.println("Resultado real: " + b);
        System.out.println("Error de redondeo: " + (1.0 - b));
    }
}
```

---

### Ejemplo funcional en Java

```java
public class ErrorRedondeo {
    public static void main(String[] args) {
        double resultado = (1.0 / 3.0) * 3.0;
        double esperado = 1.0;

        System.out.println("Resultado calculado: " + resultado);
        System.out.println("Resultado esperado: " + esperado);
        System.out.println("Error de redondeo: " + Math.abs(esperado - resultado));
    }
}
```

---

### Caso de prueba:

```
Resultado calculado: 0.9999999999999999  
Resultado esperado: 1.0  
Error de redondeo: 1.1102230246251565E-16
```
### [<- Regresar a T1 - Introducción a los Métodos Numéricos](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ae1f13f7ca5adf0391f0615d7c2a904a1cbd981c/T1/Introducci%C3%B3n%20a%20los%20Metodos%20Numericos.md)
