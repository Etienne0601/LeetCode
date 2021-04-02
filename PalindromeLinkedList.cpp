#include <iostream>
#include <vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
private:
    bool reverseCheck(vector<int>& toCheck, ListNode* checkPtr) {
        int i;
        ListNode* currPtr = checkPtr;
        // first check if it's an even-numbered palindrome
        for (i = toCheck.size() - 1; i >= 0 && currPtr != nullptr; --i) {
            if (toCheck[i] != currPtr->val) {
                break;
            }
            currPtr = currPtr->next;
        }
        if (i == -1 && currPtr == nullptr) {
            // then it's a valid even-numbered palindrome
            return true;
        }

        // now check if it's an odd-numbered palindrome
        currPtr = checkPtr;
        for (i = toCheck.size() - 2; i >= 0 && currPtr != nullptr; --i) {
            if (toCheck[i] != currPtr->val) {
                break;
            }
            currPtr = currPtr->next;
        }

        return (i == -1 && currPtr == nullptr);
    }
public:
    bool isPalindrome(ListNode* head) {
        // check the trivial case first
        if (head->next == nullptr) {
            return true;
        }
        vector<int> vals;
        ListNode* currPtr = head;
        while (currPtr != nullptr) {
            if (reverseCheck(vals, currPtr)) {
                return true;
            }
            vals.push_back(currPtr->val);
            currPtr = currPtr->next;
        }
        return false;
    }
};