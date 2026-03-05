//program that takes two numbers from user and performs all 4 basic arithmetic operations.
#include <iostream>
using namespace std;

int main() {
    double x, y, add, diff, prod, quot;
    cout << "Enter first number : ";
    cin >> x;
    cout << "Enter second number : ";
    cin >> y;
    
    add = x + y;
    diff = x - y;
    prod = x * y;

    if (y == 0) {
        cout << "Division by zero is not possible" << '\n';
    }

    else {
        quot = x / y;
        cout << "Quotient of " << x << " and " << y << " is " << quot << '\n';
    }

    cout << "Sum of " << x << " and " << y << " is " << add << '\n';
    cout << "Difference of " << x << " and " << y << " is " << diff << '\n';
    cout << "Product of " << x << " and " << y << " is " << prod << '\n';

    return 0;
}