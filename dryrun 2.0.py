grade = int(input('what did grade did you get on the test?'))

if grade >= 97 and grade <= 100:
    print('A+')

elif grade <97 and grade >= 93:
    print('A')

elif grade < 93 and grade >=90:
    print('B+')

elif grade < 90 and grade >= 87:
    print('B')

elif grade < 87 and grade >= 83:
    print('B-')

elif grade < 83 and grade >=80:
    print('C')

else:
    print('F')