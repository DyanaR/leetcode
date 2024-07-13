class Solution
{
public:
    int characterReplacement(string s, int k)
    {
        int maxLength = 0;
        unordered_map<char, int> umap;
        int left = 0;
        int charCount = 0;

        for (int right = 0; right < s.length(); right++)
        {
            char currentChar = s[right];
            umap[currentChar]++;                           // keeps count of each char
            charCount = max(charCount, umap[currentChar]); // count of max char
            int length = right - left + 1;
            // decrease sliding window to make it valid if greater than k
            if (length - charCount > k)
            {
                umap[s[left]]--;           // decrement the char in umap thats not in the
                                           // sliding window
                left++;                    // move the left pointer
                length = right - left + 1; // update the sliding window length
            }
            maxLength = max(maxLength, length);
        }
        return maxLength;
    }
};