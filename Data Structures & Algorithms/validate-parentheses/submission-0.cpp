class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        unordered_map<char, char>pairs={{')','('}, 
                                        {']','['}, 
                                        {'}','{'}};
        for(char c:s)
        {
            if(pairs.count(c))
            {
                if(!stck.empty() && stck.top()==pairs[c])
                {
                    stck.pop();
                }
                else
                {
                    return false;
                }
            }
            else{
                stck.push(c);
            }
        }
        return stck.empty();
    }
};
