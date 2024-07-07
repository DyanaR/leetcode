class Solution
{
public:
    bool isPalindrome(string s)
    {
        // make all lowercase
        //  remove spaces
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        s.erase(std::remove_if(s.begin(), s.end(),
                               [](char c)
                               { return !std::isalnum(c); }),
                s.end());

        // using two points, 1 at start and 1 at end
        //  compare both pointers, must be the same
        int start = 0;
        int end = s.size() - 1;
        while (start <= end)
        {
            if (s[start] != s[end])
            {
                return 0;
            }
            start++;
            end--;
        }
        return 1; // false
    }
};