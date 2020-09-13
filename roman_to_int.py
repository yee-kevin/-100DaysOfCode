class Solution:
    def romanToInt(self, s):
        sum = 0     
        for i in range(len(s)):
            if s[i] == 'I':             
                sum += 1
            if s[i] == 'V':             
                sum += 5
                if s[i-1] == 'I' and i!=0:
                    sum -= 2
            if s[i] == 'X':
                sum += 10
                if s[i-1] == 'I' and i!=0:
                    sum -= 2
            if s[i] == 'L':
                sum += 50
                if s[i-1] == 'X' and i!=0:
                    sum -= 20
            if s[i] == 'C':
                sum += 100
                if s[i-1] == 'X' and i!=0:
                    sum -= 20
            if s[i] == 'D':
                sum += 500
                if s[i-1] == 'C' and i!=0:
                    sum -= 200
            if s[i] == 'M':
                sum += 1000
                if s[i-1] == 'C' and i!=0:
                    sum -= 200
        return sum

print(Solution().romanToInt("MCMXCIV"))