// 0-1 Knapsack (Dynamic Programming)
#include <iostream>
using namespace std;

int main() {
    int n, W;
    cout << "Enter number of items: ";
    cin >> n;

    int weight[50], profit[50];
    cout << "Enter weight and profit of each item:\n";
    for (int i = 1; i <= n; i++)
        cin >> weight[i] >> profit[i];
    cout << "Enter knapsack capacity: ";
    cin >> W;

    int dp[51][101];   // dp[i][w] = best profit using first i items with capacity w

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (weight[i] <= w)
                dp[i][w] = max(dp[i - 1][w], profit[i] + dp[i - 1][w - weight[i]]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }

    cout << "\nMaximum profit = " << dp[n][W] << endl;

    // find which items were picked
    cout << "Items selected: ";
    int w = W;
    for (int i = n; i >= 1; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << i << " ";
            w -= weight[i];
        }
    }
    cout << endl;
    return 0;
}
