# ** creates a dict
# *args is different arugments

def foo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


def main():
    foo('test', 'hello', 1,3,4,5,6, total=100, milk = 400)

if __name__ == '__main__':
    main()