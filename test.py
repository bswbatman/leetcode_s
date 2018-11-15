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