name = "John Jay"


def find_j(s,c):

    char_count = 0
    for i in range(len(s)):
        if s[i] == c:
            char_count += 1
    return char_count


f = find_j(name, 'J')
print(f)