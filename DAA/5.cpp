// N-Queens Problem (Backtracking)
#include <iostream>
using namespace std;

int n;
int board[20][20];
int solCount = 0;

// can we place a queen at (row, col)?
bool isSafe(int row, int col) {
    // check same column above
    for (int i = 0; i < row; i++)
        if (board[i][col] == 1) return false;

    // check upper-left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1) return false;

    // check upper-right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
        if (board[i][j] == 1) return false;

    return true;
}

void printBoard() {
    solCount++;
    cout << "\nSolution " << solCount << ":\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout << (board[i][j] ? "Q " : ". ");
        cout << endl;
    }
}

void solve(int row) {
    if (row == n) {          // all queens placed
        printBoard();
        return;
    }
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;     // place queen
            solve(row + 1);          // go to next row
            board[row][col] = 0;     // backtrack
        }
    }
}

int main() {
    cout << "Enter N: ";
    cin >> n;

    solve(0);

    cout << "\nTotal solutions = " << solCount << endl;
    return 0;
}
