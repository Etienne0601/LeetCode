#include <bitset>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;


pair<int,int> operator+(const pair<int,int> & l,const pair<int,int> & r) {   
    return make_pair(l.first+r.first, l.second+r.second);                                    
}

class Solution {
private:
    pair<int,int> stringToPair(string& str) {
        int zeros = 0, ones = 0;
        for (string::const_iterator itr = str.cbegin(); itr != str.cend(); ++itr) {
            (*itr == '0') ? ++zeros : ++ones;
        }
        return make_pair(zeros, ones);
    }
    unsigned int baseTwoExp(unsigned int input) {
        if (input <= 0) {
            return 1;
        } else {
            return 2 * baseTwoExp(input - 1);
        }
    }
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        unsigned int size = strs.size();
        vector<pair<int,int>> pairs;
        unsigned int possibleSubsets = baseTwoExp(size);
        int output = 0;
        int numIncluded;
        for (unsigned int i = 0; i < size; ++i) {
            pairs.push_back(stringToPair(strs[i]));
        }
        for (unsigned int i = 1; i <= possibleSubsets; ++i) {
            bitset<600> select(i);
            numIncluded = 0;
            pair<int,int> total(0, 0);
            for (unsigned int j = 0; j < size; ++j) {
                if (select[j]) {
                    total = total + pairs[j];
                    ++numIncluded;
                }
            }
            if (total.first <= m && total.second <= n && numIncluded > output) {
                output = numIncluded;
            }
        }
        return output;
    }
};