#--1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in range(nums.index(i)+1,len(nums)):
                sums = i + nums[j]
                if sums == target:
                    return [nums.index(i),j]


#--7
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # l = len(str(x))
        k = 0
        nu =0
        p = 0
        for i in str(x):
            if i == '-':
                p =1
                continue
            nu += int(i)*(10**k)
            #print(nu)
            k += 1
        nu = int('-'*p + str(nu))
        if -2147483648<nu<2147483648:
            return nu
        else:
            return 0

#--9
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        a = str(x)[::-1]
        if int(a) == x:
            return True
        else:
            return False

#--fast
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x >= 0 and str(x) == str(x)[::-1]:
            a = True
        else:
            a = False
        return a
