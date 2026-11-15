// Fractional Knapsack (Greedy)
#include <iostream>
#include <algorithm>
using namespace std;

struct Item {
    int weight;
    int profit;
    double ratio;     // profit / weight
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

int main() {
    int n;
    double capacity;
    cout << "Enter number of items: ";
    cin >> n;

    Item items[50];
    cout << "Enter weight and profit of each item:\n";
    for (int i = 0; i < n; i++) {
        cin >> items[i].weight >> items[i].profit;
        items[i].ratio = (double)items[i].profit / items[i].weight;
    }
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    sort(items, items + n, compare);

    double totalProfit = 0;
    for (int i = 0; i < n; i++) {
        if (capacity >= items[i].weight) {          // take whole item
            capacity -= items[i].weight;
            totalProfit += items[i].profit;
        } else {                                    // take a fraction
            totalProfit += items[i].ratio * capacity;
            break;
        }
    }

    cout << "\nMaximum profit = " << totalProfit << endl;
    return 0;
}
