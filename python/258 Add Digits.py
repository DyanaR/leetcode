class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            strNum = str(num)
            total = 0 
            for x in strNum:
                digit = int(x)
                total += digit
            num = total 
        return num