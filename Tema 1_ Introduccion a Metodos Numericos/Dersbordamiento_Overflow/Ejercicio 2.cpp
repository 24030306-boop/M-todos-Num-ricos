#include <iostream>
#include <limits>

int main() {
    double maximo = std::numeric_limits<double>::max();
    std::cout << "Valor máximo de double: " << maximo << std::endl;

    double resultado = maximo * 2;
    std::cout << "Resultado después del overflow: " << resultado << std::endl;

    if (resultado == std::numeric_limits<double>::infinity()) {
        std::cout << "ERROR: Overflow detectado (infinito)" << std::endl;
    }

    return 0;
}
