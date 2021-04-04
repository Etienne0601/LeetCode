#include <iostream>
#include <list>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        // bases cases for lengths 0 and 1
        if (s.length() <= 1) {
            return 0;
        }
        // create doubly linked list from the input string, with the following encoding:
        // 0 = '('
        // 1 = ')'
        // 2+ = number representing itself
        list<unsigned int> strMod;
        bool hasNoValids = true;

        // fill the doubly linked list
        for (string::const_iterator itr = s.cbegin(); itr != s.cend(); ++itr) {
            char curr = *itr;
            curr -= '(';
            strMod.push_back((unsigned int)curr);
        }

        list<unsigned int>::iterator prev, next;
        // scan through the list, replacing "()" with '2'
        list<unsigned int>::iterator scanItr = strMod.begin();
        ++scanItr;
        while (scanItr != strMod.end()) {
            prev = scanItr;
            --prev;
            if (*prev == 0 && *scanItr == 1) {
                hasNoValids = false;
                *scanItr = 2;
                strMod.erase(prev);
            }
            ++scanItr;
        }

        if (hasNoValids) {
            return 0;
        }

        bool performedActions = true;
        // while we're not done i.e. there's no way to collapse strMod further
        while (strMod.size() > 1 && performedActions) {
            performedActions = false;
            for (list<unsigned int>::iterator itr = strMod.begin(); itr != strMod.end(); ++itr) {
                prev = next = itr;
                ++next;
                if (next == strMod.end() || *itr < 2) {
                    continue;
                }
                if (itr != strMod.begin()) {
                    // perform the "enclosed" check
                    --prev;
                    if (*prev == 0 && *next == 1) {
                        performedActions = true;
                        *itr += 2;
                        strMod.erase(prev);
                        strMod.erase(next);
                        continue;
                    }
                }
                // perform the "adjacent" check
                if (*next >= 2) {
                    performedActions = true;
                    *itr = *itr + *next;
                    strMod.erase(next);
                }
            }
        }

        // now, strMod is fully collapsed, and we simply
        // need to find the largest number >= 2
        unsigned int output = 0;
        for (list<unsigned int>::const_iterator itr = strMod.cbegin(); itr != strMod.cend(); ++itr) {
            if (*itr >= 2 && *itr > output) {
                output = *itr;
            }
        }
        return (int)output;
    }
};