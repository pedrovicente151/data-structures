class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data) == 0
