class Solution
{
public:
    string encode(vector<string> &strs)
    {
        string encoded;
        for (auto &x : strs)
        {
            encoded = encoded + to_string(x.size()) + '#' + x;
        }
        return encoded;
    }

    vector<string> decode(string s)
    {
        vector<string> decoded;
        int i = 0;
        while (i < s.size())
        {
            // Find the position of the delimiter '#'
            int j = i;
            while (s[j] != '#')
            {
                j++;
            }

            int numberOfSkips = stoi(s.substr(i, j - i));

            j++;

            string str = s.substr(j, numberOfSkips);
            decoded.push_back(str);

            i = j + numberOfSkips;
        }
        return decoded;
    }
};