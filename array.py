class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty/')
        return self.data.pop()

    def see_top(self):
        temp = self.data.pop()
        temp1 = self.data.pop()

        self.push(temp)
        self.push(temp1)

        return temp, temp1



def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.strip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


def is_matched(expr):
    left = '({['
    right = ')}]'
    S = ArrayStack()
    for i in expr:
        if i in left:
            S.push(i)
        elif i in right:
            if S.is_empty():
                return False
            if right.index(i) != left.index(S.pop()):
                return False
    return S.is_empty()
