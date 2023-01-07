class Stack:
    def __init__(self):
        self.__vector = []

    def is_empty(self):
        return len(self.__vector) == 0

    def push(self, element):
         self.__vector.append(element)

    def pop(self):
        if not self.is_empty():
            return self.__vector.pop()
        else:
            return "Empty"

    def len(self):
        return len(self.__vector)

    def print(self):
        return self.__vector

    def top(self):
        return self.__vector[-1]
