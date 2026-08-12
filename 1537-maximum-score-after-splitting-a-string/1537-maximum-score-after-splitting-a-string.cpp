class Solution {
public:
    int maxScore(string s) {

        size_t size = s.size();
        int answer = 0;
        vector<char> left;
        vector<char> right;
        left.push_back(s[0]);
        right.insert(right.end(), s.begin()+1, s.end());

        while(size > 1){

            int left_sum = count(left.begin(), left.end(), '0');
            int right_sum = count(right.begin(), right.end(), '1');

            int max = left_sum + right_sum;

            if (max>answer){
                answer=max;
            }

            char temp= right.front();
            right.erase(right.begin());
            left.push_back(temp);

            size--;
        }

        return answer;
    }

};