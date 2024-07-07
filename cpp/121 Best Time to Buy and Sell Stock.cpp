// BRUTE FORCE
// Time Complexity: O(n)

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int maxTotal = 0;
        for (int i = 0; i < prices.size(); i++)
        {
            int j = i + 1;
            while (j < prices.size())
            {
                int total = prices[j] - prices[i];
                maxTotal = max(maxTotal, total);
                j++;
            }
        }
        if (maxTotal <= 0)
        {
            return 0;
        }
        else
        {
            return maxTotal;
        }
    }
};

// EFFICIENT SOLUTION
// Time Complexity: O(n)
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int buy = prices[0];
        int maxTotal = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            // find the lowest price to buy
            // if lower price found, update it
            if (prices[i] < buy)
            {
                buy = prices[i];
            }
            maxTotal = max(maxTotal, prices[i] - buy);
        }
        return maxTotal;
    }
};