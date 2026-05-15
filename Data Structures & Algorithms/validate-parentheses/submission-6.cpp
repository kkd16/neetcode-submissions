class Solution {
public:
    bool isValid(string s) {

        unordered_map<char, char> pairs = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        stack<int> stk;

        for (auto c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stk.push(c);
            } else {
                if (stk.empty() || stk.top() != pairs[c]) {
                    return false;
                }
                stk.pop();
            }
        }

        return stk.empty();
        
    }
};
