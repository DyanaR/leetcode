class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        // track longest subsequence
        int longestLength = 0;
        // hash map to store each int in nums and track its boolean state
        // key = int , value = boolean state
        unordered_map<int, bool> umap;
        // intialize the map with false values
        for (auto &num : nums)
        {
            umap[num] = false;
        }

        for (auto &num : nums)
        {
            // if visited (true) then skip it
            if (umap[num])
                continue;

            int currentLength = 1;
            umap[num] = true; // 47 = true

            // increment - forward direction
            int nextNum = num + 1; // 47+1 = 48
            // go through the keys to try to find it and it's value is false
            // so while nextNum is found and is false do the following...
            while (umap.find(nextNum) != umap.end() && umap[nextNum] == false)
            {
                currentLength++;
                umap[nextNum] = true;
                nextNum++;
            }

            // decrement - backward direction
            int prevNum = num - 1;
            while (umap.find(prevNum) != umap.end() && umap[prevNum] == false)
            {
                currentLength++;
                umap[prevNum] = true;
                prevNum--;
            }

            // updates longestLength with currentLength if its greater than
            // the current longestLength
            longestLength = max(longestLength, currentLength);
        }

        return longestLength;
    }
};