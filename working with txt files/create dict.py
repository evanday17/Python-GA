def read_file(f):
    file = open(f, 'r')
    d = {}

    try: # iterates through each line of the file
        for line in file:
            col = line.split(';')  # split the data by ;
            d[col[0]] = {col[1], float(col[2])} #  i had return inside the for loop that is why it kept repeating
        return d
    except FileNotFoundError:

        print(f, ' is not exists')
    finally:
        file.close()

if __name__ == '__main__':
    data = read_file('data2.txt')
    print(data)