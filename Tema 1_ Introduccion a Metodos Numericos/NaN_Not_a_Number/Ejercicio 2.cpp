#include <iostream>
#include <cmath>

int main() {
    double a = 0.0;
    double b = 0.0;
    double resultado = a / b;

    std::cout << "Resultado: " << resultado << std::endl;

    if (std::isnan(resultado)) {
        std::cout << "ERROR: Resultado indefinido (NaN)" << std::endl;
    }

    return 0;
}
