#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    double a = 0.1 + 0.1 + 0.1;
    double b = 0.3;

    std::cout << std::setprecision(17);
    std::cout << "Valor de a (0.1 * 3): " << a << std::endl;
    std::cout << "Valor de b: " << b << std::endl;

    std::cout << "\n--- Comparacion con '==' ---" << std::endl;
    if (a == b) {
        std::cout << "Resultado: Son iguales" << std::endl;
    } else {
        std::cout << "Resultado: SON DIFERENTES (Error esperado)" << std::endl;
    }

    double epsilon = 0.00001;
    std::cout << std::setprecision(6);
    std::cout << "\nComparacion con Epsilon (" << epsilon << ")" << std::endl;
    if (std::abs(a - b) < epsilon) {
        std::cout << "Resultado: Son iguales (dentro del margen de error)" << std::endl;
    } else {
        std::cout << "Resultado: Son diferentes" << std::endl;
    }

    return 0;
}
