'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

class Solution:
    def isPalindrome(self,num):
        string = str(num)
        if '-'in string:
            return False
        else:
            newStr = ""
            emptyList = []
            for i in range(len(string)):
                emptyList.append(int(string[i]))
            emptyList.reverse()
            for items in emptyList:
                newStr = newStr+str(items)
            return newStr == string