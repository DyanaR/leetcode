class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> seen;
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++)
        {
            char currentChar = s[right];
            if (seen.find(currentChar) != seen.end() &&
                seen[currentChar] >= left)
            {
                // update left pointer past the first occurance of the repeated
                // character
                left = seen[currentChar] + 1;
            }
            seen[currentChar] = right;

            int length = right - left + 1;

            maxLength = max(maxLength, length);
        }
        return maxLength;
    }
};