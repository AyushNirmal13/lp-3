#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    // Each item stores: {frequency, "characters"}
    vector<pair<int, string>> list(n);
    string code[256]; // Stores final binary code for each ASCII character

    // Step 1: Read input
    for (int i = 0; i < n; i++) {
        char ch;
        cin >> ch >> list[i].first;
        list[i].second = ch; // Convert single char to string
    }

    // Special case: Only 1 character
    if (n == 1) {
        char singleChar = list[0].second[0];
        code[singleChar] = "0";
    }

    // Step 2: Keep merging the 2 smallest items until 1 remains
    while (list.size() > 1) {
        sort(list.begin(), list.end()); // Smallest two move to index 0 and 1

        // Add '0' in front of all characters in the 1st smallest group
        for (char c : list[0].second) {
            code[c] = "0" + code[c];
        }

        // Add '1' in front of all characters in the 2nd smallest group
        for (char c : list[1].second) {
            code[c] = "1" + code[c];
        }

        // Merge item 0 and item 1 into item 0
        list[0].first += list[1].first;     // Add frequencies
        list[0].second += list[1].second;   // Combine character strings

        // Remove item 1
        list.erase(list.begin() + 1);
    }

    // Step 3: Print all generated codes
    for (int i = 0; i < 256; i++) {
        if (code[i] != "") {
            cout << char(i) << " : " << code[i] << endl;
        }
    }

    return 0;
} 



//input 
// 6
// a 5
// b 9
// c 12
// d 13
// e 16
// f 45



// output 
// a : 1100
// b : 1101
// c : 100
// d : 101
// e : 111
// f : 0










    
