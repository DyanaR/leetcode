class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = [] # convert to string later
        letter_counter = 0
        flag = True
        first = strs[0] # use the first word to check against
        
        for letter in first: 
            for word in strs:
                if len(word)-1 < letter_counter:
                    flag = False
                    break
                elif first[letter_counter] == word[letter_counter]:
                    flag = True
                    continue
                else:
                    flag = False
                    break 
        
            if flag == True:
                result.append(first[letter_counter])
                letter_counter += 1
            else:
                break

        str_result = ''.join(result) 

        return str_result


# Time Complexity: O(n * m)
# Space Complexity: O(m)
# n= # of words in strs
# M = length of shortest string in strs
