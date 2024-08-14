class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for x in s:
            if 65 <= ord(x) <= 90: 
                lower_dec = ord(x) + 32
                result += chr(lower_dec)
            else:
                result += x
        return result
        