
package T4.Problemario;

public class Metodo_Interpolación {
    public static double interpolate(double[] x, double[] y, double xVal) {
        double result = 0.0;
        for (int i = 0; i < x.length; i++) {
            double term = y[i];
            for (int j = 0; j < x.length; j++) {
                if (j != i) {
                    term *= (xVal - x[j]) / (x[i] - x[j]);
                }
            }
            result += term;
        }
        return result;
    }
    public static void main(String[] args) {
        double[] x = {1, 3, 4};
        double[] y = {2, 5, 6};
        double xVal = 2;
        System.out.printf("Interpolación Lagrange en x=%.2f: %.4f\n", xVal,
                interpolate(x, y, xVal));
    }
}