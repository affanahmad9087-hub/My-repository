#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "enter a number : ";
    cin >> n;
    if (n > 0){
        cout << n << " is a positive number." << '\n'; 
    }
    else if (n < 0){
        cout << n << " is a negative number." << '\n';
    }
    else{
        cout << n << " is neither positive nor negative." << '\n';
    }
    return 0;
}