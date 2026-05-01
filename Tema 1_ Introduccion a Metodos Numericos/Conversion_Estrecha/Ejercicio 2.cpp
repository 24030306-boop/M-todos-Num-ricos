#include <iostream>

int main() {
    double valorDouble = 3.14159e10;
    int valorInt = (int) valorDouble;

    std::cout << "Valor Original: " << valorDouble << std::endl;
    std::cout << "Valor Truncado: " << valorInt << std::endl;

    return 0;
}
