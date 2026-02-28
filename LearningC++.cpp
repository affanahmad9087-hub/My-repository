#include <iostream>

int main() {// This is a simple C++ program that prints "Hello, World!" to the console.
    std::cout << "Hello, World!" << std::endl;// The std::cout is used to output the text to the
    //  console, and std::endl is used to insert a newline character after the output.
    //instead of std::endl we can use '\n' a newline character wihich is better performance wise.
    //VARIABLES:
    //two steps are used to create a variable, DECLERATION and ASSIGNMENT.
    //DECLARATION: List the data type of the variable.
    int x;//Decleration. int is used to specify that the identifier or 'x' is being used to store
    //an integer value or a whole number value. 
    x = 5;//this is assignment, the identifier for the integer, x is given a value of 5.
    std::cout << x << '\n';//display the variable x
    //so the general form of a variable in c++ is 
    // {data_type_of_the_variable} {identifier (or id for short)};
    // {id} = {value (should correspond to data_type_of_the_variable as declared earlier)}
    //data types in c++: int, double, float, char, bool.
    //instead of using two lines, one for decleration and one for assignment, a oneliner
    //shorthand assignment can be used for a variable.  
    float y = 5.6;//example for shorthand / oneliner assignment for variables.
    std::cout << y << '\n';
    //adding x and y
    float sum = x + y;
    std::cout << sum << '\n';//displays the value of the sum variable which is a float hence the 
    // float decleration, which is 5 + 5.6 = 10.6.
    //if a float value is declared as an int value, the decimal or the float part is truncated.
    //for example:
    int balance = 900.897;
    std::cout << balance << '\n';//prints 900 instead of 900.897.
    //another data type is char which stores a single character. If two characters are provided
    //it returns only the last character.
    //also int is a 4byte data type and char is a 1 byte data type, 
    //so if we assign a char value to an int variable
    char z = 'A';
    int z_int = z;
    std::cout << z_int << '\n';//prints 65, which is the ASCII value of 'A'.
    //also a double data type is used to store decimal values with double precision, 
    //which means it can store more decimal places than a float.
    //double is an 8 byte data type, while float is also a  4 byte data type.
    /*When you try to fit a 64-bit double (like 3.14) into a 32-bit int,
        the compiler essentially "chops off" everything after the decimal point. 
        You don't get 3.14; you just get 3.
        The danger here is data loss. While 3.14 to 3 seems small, 
        doing this with large numbers or in complex calculations can break your program's logic. 
        Modern C++ compilers will usually give you a warning ⚠️ about this, 
        but they will still let the code run.*/
        /*the sizeof() function tells exactly how many bytes a data type uses in memory*/
    std::cout << "Size of int: " << sizeof(int) << " bytes\n";//prints the size of int data type in bytes, which is 4 bytes.
    std::cout << "Size of float: " << sizeof(float) << " bytes\n";//prints the size of float data type in bytes, which is 4 bytes.
    std::cout << "Size of double: " << sizeof(double) << " bytes\n";//prints the size of double data type in bytes, which is 8 bytes.
    std::cout << "Size of char: " << sizeof(char) << " bytes\n";//prints the size of char data type in bytes, which is 1 byte.
    /* to prevent the accidental data narrowing, C++17 introduced a new feature called "narrowing conversion".
    This feature allows the compiler to detect and prevent implicit conversions that may lead to data loss.
    this is invoked using the "narrowing conversion" syntax, which is a double curly brace initialization.
    */
    
    return 0;// The return statement indicates that the program ended successfully.
            // if the program returns 0, it means that it executed without any errors.
            // if it returns a non-zero value, it indicates that an error occurred during 
            // execution.
}
