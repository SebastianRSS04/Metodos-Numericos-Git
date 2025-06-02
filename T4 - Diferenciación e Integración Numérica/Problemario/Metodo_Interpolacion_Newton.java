
package T4.Problemario;

public class Metodo_Interpolacion_Newton {
   public static double interpolate(double[] x, double[] y, double xVal)
   {
       double[] coef = y.clone();
       int n = x.length;
       // Cálculo de diferencias divididas
       for (int j = 1; j < n; j++) {
           for (int i = n - 1; i >= j; i--) {
               coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j]);
           }
       }
       return coef[n - 1];
   }
// Evaluación del polinomio
   public static double evaluate(double[] x, double[] y, double xVal) {
       double result = y[0];
       for (int i = 1; i < x.length; i++) {
           double term = y[i];
           for (int j = 0; j < i; j++) {
               term *= (xVal - x[j]) / (x[i] - x[j]);
           }
           result += term;
       }
       return result;
   }
   public static void main(String[] args) {
       double[] x = {1, 3, 4};
       double[] y = {2, 5, 6};
       double xVal = 2;
       System.out.printf("Interpolación Newton en x=%.2f: %.4f\n", xVal,
               evaluate(x, y, xVal));
   }
}
