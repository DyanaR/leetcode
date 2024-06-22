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
        for (int i = 0; i < s.size(); i++)
        {
            while (s[i] != '#')
            {
                i++;
            }
            int numberOfSkips = stoi(s.substr(i - 1, 1));
            string str = s.substr(i + 1, numberOfSkips);
            decoded.push_back(str);
            i = i + numberOfSkips;
        }
        return decoded;
    }
};