'''try:
    a = 5
    b = '0'
    print(a+b)
except TypeError:
    print('unsupported operation')
print('Out of try except blocks')'''

'''try:
    x = input('Enter a number up to 100: ')
    if x > 100:
        raise TypeError(x)
except TypeError:
    print(x, 'is out of allowed range')
else:
    print(x, 'is within the allowed range')'''

try:
    num1 = int(input('please enter 1 number'))
    num2 = int(input('please enter another number'))
    if num1 and num2 != int:
        raise ValueError(num1, num2)
except ValueError:
    print('that is not a number')
else:
    print('passed')
