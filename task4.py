from task1 import stack

def is_balanced(expression):
    Stack = stack()
    opening = "({["
    closing = ")}]"
    mapping = {')': '(', '}': '{', ']': '['}
    
    for ch in expression:
        if ch in opening:
            Stack.push(ch)
        elif ch in closing:
            if Stack.is_empty() or Stack.pop() != mapping[ch]:
                return False
    return Stack.is_empty()


def main():
    print(is_balanced("(a+b)"))
    print(is_balanced("{[()]}"))
    print(is_balanced("((a+b]"))


if __name__ == "__main__":
    main()

