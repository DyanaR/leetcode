class Solution:
    def isValid(self, s: str) -> bool:
        arrayS = list(s)
        length = len(arrayS)
        stack = []
        if length % 2 != 0:
            return False

        for x in arrayS:
            # push first element
            # if len(stack) = 0:
            if x == "(" or x == "{" or x == "[":
                stack.append(x) # add to stack
            else:
                if not stack: # if first element is closing
                    return False

                last = stack[-1] #grab element on top of stack
                # if matching pairs then pop
                if (
                    (x == ")" and last == "(")
                    or (x == "]" and last == "[")
                    or (x == "}" and last == "{")
                ):
                    stack.pop()
                else:
                    return False
        #if stack empty return true 
        return len(stack) == 0
