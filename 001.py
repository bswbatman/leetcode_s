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

#--fast9
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

#--13  #cant use
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dii = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        summ = 0
        summm = 0
        listt = list(s)
        lenn = len(listt)
        k = 0

        j = 0
        for i in range(lenn):
            print('--------------------------------------')
            print('i1', i)
            i += k
            if j - i == 1:
                i = j + 1
            # print(listt)

            print('i2', i)
            if i == lenn - 1:
                print('gg')
                summm += dii[listt[lenn - 1]]
                break
            if (i + 1) > lenn - 1:
                break
            if dii[listt[i]] <= dii[listt[i + 1]]:
                summ += dii[listt[i + 1]] - dii[listt[i]]
                summm += dii[listt[i + 1]] - dii[listt[i]]
                print('make', listt[i])
                # print('i',i)
                k += 1
                if summ == 0:
                    summm += dii[listt[i]]
                    print('summm:', summm)
                    k = 0
                print('sum1', summm)
                print('k:', k)
                print('i:', i)
                j = i
            else:
                k = 0
                print('strart')
                summm += dii[listt[i]]
                # if dii[listt[i]] > dii[listt[i+1]]:
                #     k = 1
                print('make：', listt[i])
                print('sum2', summm)
                print('k:', k)
                print('i:', i)
                j = i

        return summm
