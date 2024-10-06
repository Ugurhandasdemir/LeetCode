class Solution {
public:
    bool isValid(string s) {
        stack<char> tut;
        string count;
        bool answer;

        for(int i=0; i<s.size();i++){
            if(s[i] == '(' || s[i] == '{' || s[i] == '[' ){
                tut.push(s[i]);
            }
            else{
                if(tut.empty() || (s[i]==')' && tut.top() != '(') || (s[i]==']' && tut.top() != '[') || (s[i]=='}' && tut.top() != '{')){
                    return false;
                }
                tut.pop();
            }
        }

    return tut.empty();
        
    }
};