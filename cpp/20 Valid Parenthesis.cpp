class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> myStack;

        if (s.length() % 2 != 0)
        {
            return false;
        }

        for (char c : s)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                myStack.push(c);
            }
            else
            { // if closing bracket
                if (myStack.empty())
                {
                    return false;
                }
                char last = myStack.top();
                if (c == ')' && last == '(' || c == '}' && last == '{' ||
                    c == ']' && last == '[')
                {
                    myStack.pop();
                }
                else
                {
                    return false; // miss matched brackets
                }
            }
        }
        // if stack is empty then we went through whole string, it was valid,
        // and return true else false
        return myStack.empty();
    }
};