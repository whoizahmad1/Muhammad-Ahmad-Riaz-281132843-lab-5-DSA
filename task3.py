from task1 import stack

def reverse_st(input_str):
    Stack = stack()
    for i in input_str:
        Stack.push(i)
    
    reverse_str = ""
    while not Stack.is_empty():
        reverse_str += Stack.pop()
    return reverse_str

def main():
    print(reverse_st("hello"))
    print(reverse_st("hiiii"))

if __name__== "__main__":
    main()
