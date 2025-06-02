## Tema 1: Error Numerico Total

## ¿Que es? 

El error numérico total es la combinación de todos los errores que pueden surgir en un cálculo numérico . Representa errores de redondeo, truncamiento, errores del modelo matemático e incluso errores por cancelación o incertidumbre en los datos de entrada .

lidad de los resultados obtenidos con métodos numéricos. Este análisis permite decidir qué método aplicar, cuántas iteraciones realizar o cuánta precisión es necesaria en los datos iniciales para obtener un resultado aceptable.

### Ventajas y Desventajas

#### Ventajas
- **Evaluación integral**: Permite cuantificar el impacto combinado de todos los errores en un cálculo, ofreciendo una visión completa de la precisión del resultado.
- **Toma de decisiones informada**: Ayuda a elegir métodos numéricos adecuados y a determinar el nivel de precisión requerido para los datos o iteraciones.
- **Identificación de problemas**: Facilita la detección de fuentes de error (como redondeo o truncamiento), lo que permite optimizar algoritmos o ajustar modelos.
- **Aplicabilidad universal**: Es un concepto aplicable a cualquier método numérico, desde cálculos simples hasta simulaciones complejas.

#### Desventajas
- **Dificultad de desglose**: Puede ser complicado separar las contribuciones individuales de cada tipo de error (redondeo, truncamiento, etc.) dentro del error total.
- **Dependencia de datos precisos**: Requiere conocer el valor exacto o una aproximación muy precisa para calcular el error, lo cual no siempre es posible.
- **Costo computacional**: Analizar y minimizar el error numérico total puede requerir cálculos adicionales o métodos más complejos, aumentando el tiempo de procesamiento.
- **Limitaciones en aplicaciones prácticas**: En problemas reales con múltiples variables, el error numérico total puede ser difícil de estimar debido a la incertidumbre en los datos de entrada.

# Pseudocódigo
## Error Numérico Total
```java
        Inicio
          Definir real como real
          Definir aproximado como real
          Definir errorTotal como real
          real = sqrt(2)
          aproximado = 1.414
          errorTotal = abs(real - aproximado)
          Imprimir "Valor real: ", real
          Imprimir "Valor aproximado: ", aproximado
          Imprimir "Error numérico total: ", errorTotal
        Fin
```
# Código base
```java

    public class ErrorNumerico {
    public static void main(String[] args) {
        // Definir variables
        double real = Math.sqrt(2);
        double aproximado = 1.414;
        double errorTotal = Math.abs(real - aproximado);

        // Imprimir resultados
        System.out.println("Valor real: " + real);
        System.out.println("Valor aproximado: " + aproximado);
        System.out.println("Error numérico total: " + errorTotal);
    }
}
```


## Ejemplo en Java con salida esperada
```java
   Error Numérico Total
    public class ErrorTotal {
        public static void main(String[] args) {
            double valorReal = Math.sqrt(2);
            double valorAproximado = 1.4142;
    
            double error = Math.abs(valorReal - valorAproximado);
    
            System.out.printf("Valor real: %.3f%n", valorReal);
            System.out.printf("Valor aproximado: %.3f%n", valorAproximado);
            System.out.printf("Error numérico total: %.3f%n", error);
        }
    }

```
**Caso de prueba**
```markdown
    Valor real: 1.414  
    Valor aproximado: 1.414  
    Error numérico total: 0.000  
```

### [<- Regresar a T1 - Introducción a los Métodos Numéricos](https://github.com/SebastianRSS04/Metodos-Numericos-Git/blob/ae1f13f7ca5adf0391f0615d7c2a904a1cbd981c/T1/Introducci%C3%B3n%20a%20los%20Metodos%20Numericos.md)
