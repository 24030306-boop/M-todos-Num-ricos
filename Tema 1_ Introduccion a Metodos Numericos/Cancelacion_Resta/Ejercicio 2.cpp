#include <iostream>
#include <iomanip>

int main() {
    double x = 1234567890.1234567;
    double y = 1234567890.1234560;

    double resultado = x - y;

    std::cout.precision(20);
    std::cout << "Resultado real: " << resultado << std::endl;

    return 0;
}
