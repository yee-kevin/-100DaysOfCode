
# Final solution
class Solution():
    def lengthOfLongestSubstring(self, s):              
        tempString = ''
        maxLength = 0
        for i in s:
            if i in tempString:
                tempString = tempString[tempString.index(i)+1:]            
            tempString += i
            maxLength = max(maxLength, len(tempString))

        return maxLength

# Example of a bad solution        
# class Solution():  
#   def run(self, s):      
#     subString = ""  
#     while(len(s)>0):
#         for i in s:
#             if i not in subString:
#                 subString += i                      
#             else:
#                 self.longest_length = max(self.longest_length, len(subString))
#                 return self.run(s[subString.index(i)+1:len(s)])         
            
#   def lengthOfLongestSubstring(self, s):
#     self.longest_length = 0
#     self.run(s)
#     return self.longest_length  





print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
print (Solution().lengthOfLongestSubstring('hellohello'))
# 4
print (Solution().lengthOfLongestSubstring(''))
# 0
print (Solution().lengthOfLongestSubstring('youlikeyoulike'))
# 7
print (Solution().lengthOfLongestSubstring('lll'))
# 1
print (Solution().lengthOfLongestSubstring('1234561'))
# 6
print (Solution().lengthOfLongestSubstring('pwwkew'))
# 3
print (Solution().lengthOfLongestSubstring(' '))
# 1
print (Solution().lengthOfLongestSubstring('dvdf'))
# 3

