class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        // for each fixed index
        for (int i = 0; i < nums.size() - 2; i++)
        {
            // initialize two pointers
            int start = i + 1;
            int end = nums.size() - 1;
            // skip duplicates
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            // similar to 2sum
            while (start < end)
            {
                int total = nums[i] + nums[start] + nums[end];

                if (total == 0)
                {
                    result.push_back({nums[i], nums[start], nums[end]});
                    // skip duplicates for start pointer
                    while (start < end && nums[start] == nums[start + 1])
                        start++;
                    start++;
                    end--;
                }
                else if (total < 0)
                {
                    start++;
                }
                else
                {
                    end--;
                }
            }
        }
        return result;
    }
};