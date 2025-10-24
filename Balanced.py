#include <bits/stdc++.h>
using namespace std;

bool isBalanced(int x) {
    string s = to_string(x);
    unordered_map<int, int> count;
    for (char c : s) count[c - '0']++;

    for (auto [digit, freq] : count) {
        if (digit == 0 || freq != digit) return false;
    }
    return true;
}

class Solution {
public:
    int nextBeautifulNumber(int n) {
        for (int i = n + 1; i <= 1224444; ++i) {
            if (isBalanced(i)) return i;
        }
        return -1; // should never reach here
    }
};
