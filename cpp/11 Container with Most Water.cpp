// BRUTE FORCE
// Time Complexity: O(n^2)
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int largestArea = 0;
        for (int i = 0; i < height.size() - 1; i++)
        {
            for (int j = i + 1; j < height.size(); j++)
            {
                int width = j - i;
                int length = min(height[i], height[j]);
                int area = width * length;
                largestArea = max(largestArea, area);
            }
        }
        return largestArea;
    }
};

// EFFICIENT SOLUTION
// Time Complexity: O(n)
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int largestArea = 0;
        // pointers
        int left = 0;
        int right = height.size() - 1;

        // while pointers dont cross
        while (left < right)
        {
            int width = right - left;
            // want the min one b/c otherwise water will spill out
            int length = min(height[right], height[left]);
            int area = width * length;
            // update the largest area
            largestArea = max(largestArea, area);
            // moves the pointer that points at the lower line
            if (height[left] < height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return largestArea;
    }
};
