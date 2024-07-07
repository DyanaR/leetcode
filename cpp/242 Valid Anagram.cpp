class Solution {
public:
    bool isAnagram(string s, string t) {

        sort(s.begin(), s.end()); // art
        sort(t.begin(), t.end()); // acr
        return s==t;
    }
};