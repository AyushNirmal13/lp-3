// 0-1 Knapsack using Recursion + Memoization (take / skip)
#include <iostream>
#include <cstring>
using namespace std;

int dp[51][101];   // dp[n][W], -1 means not solved yet

int solve(int n, int wt[], int pr[], int W) {
    // base case: no items left or no capacity left
    if (n == 0 || W == 0)
        return 0;

    // already solved? return stored answer
    if (dp[n][W] != -1)
        return dp[n][W];

    // item n-1 fits in the bag: choose between take and skip
    if (wt[n - 1] <= W) {
        int take = pr[n - 1] + solve(n - 1, wt, pr, W - wt[n - 1]);
        int skip = solve(n - 1, wt, pr, W);
        return dp[n][W] = max(take, skip);
    }

    // item too heavy: must skip
    return dp[n][W] = solve(n - 1, wt, pr, W);
}

int main() {
    int n, W;
    cout << "Enter number of items: ";
    cin >> n;

    int wt[50], pr[50];
    cout << "Enter weight and profit of each item:\n";
    for (int i = 0; i < n; i++)
        cin >> wt[i] >> pr[i];
    cout << "Enter knapsack capacity: ";
    cin >> W;

    memset(dp, -1, sizeof(dp));   // fill whole table with -1

    cout << "\nMaximum profit = " << solve(n, wt, pr, W) << endl;
    return 0;
}





// Enter number of items: 4
// Enter weight and profit of each item:
// 10 60
// 20 100
// 30 120
// 15 75
// Enter knapsack capacity: 50

// Maximum profit = 235
// Items selected: 4 2 1 
