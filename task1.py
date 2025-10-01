class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    



def main():
    s= stack()
    s.push("10")
    s.push("20")
    s.push("30")
    s.push("50")
    print(s.pop())
    print(s.pop())
    print(s.peek())
    print(s.is_empty())
    print(s.size())

if __name__== "__main__":
    main()