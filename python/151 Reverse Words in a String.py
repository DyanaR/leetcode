class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        start = 0 
        end = len(lst) - 1
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        lst = " ".join(lst)
        new_s = str(lst)
        return new_s