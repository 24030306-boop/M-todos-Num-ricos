#include <iostream>
#include <iomanip>

int main() {
    double numeroGrande = 1.0e16;
    double numeroPequeno = 1.0;
    double resultado = numeroGrande + numeroPequeno;

    std::cout << "--- Demostración de Pérdida de Precisión ---" << std::endl;
    std::cout << "Número Grande:  " << numeroGrande << std::endl;
    std::cout << "Número Pequeño: " << numeroPequeno << std::endl;
    std::cout << "Suma Resultante: " << resultado << std::endl;

    if (resultado == numeroGrande) {
        std::cout << "\nRESULTADO: El número pequeño 'desapareció'." << std::endl;
        std::cout << "La suma es igual al número original debido a la falta de bits en la mantisa." << std::endl;
    }

    long double bdGrande = 1.0e16L;
    long double bdPequeno = 1.0L;
    long double bdResultado = bdGrande + bdPequeno;

    std::cout << "\n--- Solución con Mayor Precisión ---" << std::endl;
    std::cout << std::fixed << std::setprecision(1);
    std::cout << "Suma Exacta: " << bdResultado << std::endl;

    return 0;
}
