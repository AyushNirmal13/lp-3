// Fibonacci numbers with step count (iterative and recursive)
#include <iostream>
using namespace std;

int recSteps = 0;                 // counts every recursive call

int fibRecursive(int n) {
    recSteps++;
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    // ---- Iterative ----
    int iterSteps = 0;
    int a = 0, b = 1, c = 0;
    if (n == 0) c = 0;
    else if (n == 1) c = 1;
    else {
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
            iterSteps++;          // one step per loop run
        }
    }
    cout << "\nIterative: Fib(" << n << ") = " << c << endl;
    cout << "Step count (iterative) = " << iterSteps << "   -> O(n)" << endl;

    // ---- Recursive ----
    int r = fibRecursive(n);
    cout << "\nRecursive: Fib(" << n << ") = " << r << endl;
    cout << "Step count (recursive) = " << recSteps << "   -> O(2^n)" << endl;

    // ---- Print series ----
    cout << "\nSeries: ";
    int x = 0, y = 1;
    for (int i = 0; i <= n; i++) {
        cout << x << " ";
        int next = x + y;
        x = y;
        y = next;
    }
    cout << endl;
    return 0;
}
