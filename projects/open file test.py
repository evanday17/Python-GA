def read_file(f):
    file = open(f, 'r')

    try: # iterates through each line of the file
        for i in file:
            s = i.split(',')
            print(s)
            print(s)

    except FileNotFoundError:

        print(f, ' is not exists')
    finally:
        file.close()

if __name__ == '__main__':
    read_file('Transaction Log.txt')

