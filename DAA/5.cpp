// Binomial Coefficients (Dynamic Programming - Pascal's Triangle)
#include <iostream>
using namespace std;

int main() {
    int n, k;
    cout << "Enter n and k: ";
    cin >> n >> k;

    int C[50][50];

    // C(i,j) = C(i-1,j-1) + C(i-1,j)
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0 || j == i)
                C[i][j] = 1;
            else
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }

    cout << "\nC(" << n << "," << k << ") = " << C[n][k] << endl;

    cout << "\nPascal's Triangle:\n";
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= i; j++)
            cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}
