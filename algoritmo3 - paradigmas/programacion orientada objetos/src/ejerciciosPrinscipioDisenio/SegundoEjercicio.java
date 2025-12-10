package ejerciciosPrinscipioDisenio;

public class SegundoEjercicio {
    // la clase cuenta bancaria rompe single responsibility, y en el cliente/main rompe el tell dont ask
    // pasar el if al metodo de la cuentabancaria tiene saldo suficiente
    // posible solucion seria crear una clase retirar, que el metodo retirar reciba una cuentabancaria con sus geter y
    // setters corespondientes
}

//class CuentaBancaria {
//    private double saldo;
//
//    public CuentaBancaria(double saldoInicial) { this.saldo = saldoInicial; }
//
//    public double tieneSaldoSuficiente(double monto) { return monto <= saldo; }
//
//    public void retirar(double monto) { saldo -= monto; }
//}

//public class Cliente {
//    public static void main(String[] args) {
//        CuentaBancaria cuenta = new CuentaBancaria(1000);
//
//        double montoSolicitado = 500;
//        if (!cuenta.tieneSaldoSuficiente(montoSolicitado)) {
//            throws MontoInsuficienteException("No se puede retirar. Fondos insuficientes.");
//        }
//
//        cuenta.retirar(montoSolicitado);
//    }
//}
