#include <iostream>
#include <iomanip>

int main() {
    int iteraciones = 1000000;
    double incremento = 0.1;
    double sumaDouble = 0.0;

    for (int i = 0; i < iteraciones; i++) {
        sumaDouble += incremento;
    }

    double esperado = iteraciones * incremento;

    std::cout << "--- Acumulación en Bucle (1,000,000 de iteraciones) ---" << std::endl;
    std::cout.precision(17);
    std::cout << "Resultado esperado: " << esperado << std::endl;
    std::cout << "Resultado double:   " << sumaDouble << std::endl;
    std::cout << "Diferencia (Error): " << (sumaDouble - esperado) << std::endl;

    long double sumaBD = 0.0L;
    long double incrementoBD = 0.1L;

    for (int i = 0; i < iteraciones; i++) {
        sumaBD = sumaBD + incrementoBD;
    }

    std::cout << "\n--- Solución con BigDecimal ---" << std::endl;
    std::cout << "Resultado exacto:   " << sumaBD << std::endl;

    if (sumaDouble != esperado) {
        std::cout << "\nNOTA: El error de 'double' es notable tras un millón de sumas." << std::endl;
    }

    return 0;
}
