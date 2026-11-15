// Job Sequencing with Deadlines (Greedy)
#include <iostream>
#include <algorithm>
using namespace std;

struct Job {
    char id;
    int deadline;
    int profit;
};

// sort by profit, highest first
bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

int main() {
    int n;
    cout << "Enter number of jobs: ";
    cin >> n;

    Job jobs[50];
    cout << "Enter job id, deadline, profit:\n";
    for (int i = 0; i < n; i++)
        cin >> jobs[i].id >> jobs[i].deadline >> jobs[i].profit;

    sort(jobs, jobs + n, compare);

    // find max deadline = number of slots
    int maxDeadline = 0;
    for (int i = 0; i < n; i++)
        maxDeadline = max(maxDeadline, jobs[i].deadline);

    char slot[50];
    bool filled[50] = {false};
    int totalProfit = 0;

    for (int i = 0; i < n; i++) {
        // try the latest free slot on or before the deadline
        for (int j = jobs[i].deadline - 1; j >= 0; j--) {
            if (!filled[j]) {
                filled[j] = true;
                slot[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    cout << "\nJob sequence: ";
    for (int i = 0; i < maxDeadline; i++)
        if (filled[i]) cout << slot[i] << " ";
    cout << "\nTotal profit = " << totalProfit << endl;
    return 0;
}
