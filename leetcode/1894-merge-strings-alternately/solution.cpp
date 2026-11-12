#pragma GCC optimize("Ofast,unroll-loops,inline")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <iostream>
using namespace std;

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define size length

const int _ = []() {
    FAST_IO
    return 0;
}();

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0;
        string res = "";
        for (i = 0; i < min(word1.size(), word2.size()); i++) {
            res.push_back(word1[i]);
            res.push_back(word2[i]);
        }
        if (word1.size() > word2.size()) {
            res.append(word1.substr(word2.size()));
        }
        if (word2.size() > word1.size()) {
            res.append(word2.substr(word1.size()));
        }
        return res;
    }
};

