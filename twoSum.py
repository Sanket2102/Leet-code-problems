'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


class Solution:
    def twoSum(self,myList,target):
        status = False
        indice = ""
        j=0
        while status == False:
            i = j+1
            while i<len(myList):
                if myList[j]+myList[i]==target:
                    indice = [j,i]
                    status = True
                    break
                else:
                    pass
                i+=1
            j += 1
        return indice

sol = Solution()
print(sol.twoSum([3,2,4],6))