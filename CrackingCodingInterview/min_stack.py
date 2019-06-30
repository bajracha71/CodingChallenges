# 3.2 How would you design a stack which, in addition to push
# and pop,also has a function min which returns the minimum
# element? Push, pop and min should all operate in O(1) time.

# Note: Try to implement this problem using Inheritence ( I will do it later )

class Stack(object):

    def __init__(self):
        self.items = []
        self.size = 0


    def push(self, data):
        self.items.append(data)
        self.size += 1

    def pop(self):
        if self.size > 0:
            poppedItem = self.items.pop()
            self.size -= 1
            return poppedItem
        else:
            raise Exception("Stack is empty")

    def isEmpty(self):
        return self.size == 0


    def peek(self):
        if self.size > 0:
            return self.items[-1]

        else:
            raise Exception("Stack is empty")


class MinStack(object):

    def __init__(self):
        self.items = Stack()
        self.minsofar = Stack()

    def push(self, item):
        self.items.push(item)

        if self.minsofar.isEmpty():
            self.minsofar.push(item)
        else:
            # peek at misofar stack
            val = self.minsofar.peek()
            if item <= val:
                self.minsofar.push(val)

    def peek(self):
        top = self.items.peek()
        return top


    def pop(self):
        poppeditem = self.items.pop()
        peekeditem = self.minsofar.peek()
        if poppeditem == peekeditem:
            self.minsofar.pop()

        return poppeditem

    def minimum(self):
        if self.minsofar.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.minsofar.peek()





