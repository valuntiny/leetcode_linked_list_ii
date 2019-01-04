'''
to test the function of 'is' and 'is not'
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(1)
c = a
d = None

if a is b:
    print("T")
else:
    print("F")

if a is c:
    print("T")
else:
    print("F")

if d:
    print("T")
else:
    print("F")