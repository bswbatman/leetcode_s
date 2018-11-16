# for i in range(1,3):
#     print i

t = [1,2,3]
for i in range(len(t)):
    print(i)

print(t[-1])


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # len = 0
        t = []  # 结果
        u = []  # 进位
        flag = 1
        a = l1
        b = l2
        la = 0
        lb = 0
        while flag:
            try:
                v = a.val + b.val
                if (a.val + b.val) >= 10:
                    u.append(1)
                    t.append(v - 10)
                else:
                    u.append(0)
                    t.append(v)
                # a = a.next
                # b = b.next
            except:
                flag = 0

            try:
                a = a.next
                # b = b.next
                c = a.next.val
                print('1')
            except:
                try:
                    t.append(b.next.val)
                except:
                    break

            try:
                # a = a.next
                b = b.next
                c = b.next.val
                print('56666')
            except:
                try:
                    t.append(a.next.val)
                except:
                    break
        print(t)
        print(u)
        for i in range(1, len(t)):
            try:
                t[i] = t[i] + u[i - 1]
            except:
                continue
        if u[-1] == 1:
            t.append(1)
        return t

dii = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
'''
--------------------------------------M CM XC IV
strart
--------------------------------------
i1 0
i2 0
strart
make： D
sum2 500
k: 0
i: 0
--------------------------------------
i1 1
i2 1
strart
make： C
sum2 600
k: 0
i: 1
--------------------------------------
i1 2
i2 2
make X
summm: 601
sum1 601
k: 0
i: 2
--------------------------------------
i1 3
i2 3
strart
make： X
sum2 611
k: 0
i: 3
--------------------------------------
i1 4
i2 4
gg



'''