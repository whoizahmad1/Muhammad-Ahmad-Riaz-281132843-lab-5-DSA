class queue:
    def __init__(self):
        self.items =[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

def main():
    s= queue()
    s.enqueue("55")
    s.enqueue("15")
    s.enqueue("25")
    print(s.front())
    print(s.dequeue())
    print(s.front())
    print(s.dequeue())
    print(s.front())
    print(s.is_empty())
    print(s.size())

if __name__== "__main__":
    main()
