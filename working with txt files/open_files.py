# how to read the file
input_file = open('data2.txt', 'r')
print(input_file)
print(type(input_file))
input_file.close() # always close the connection to the file

#  how to read the file again

def read_file(f):
    file = open(f, 'r')

    try: # iterates through each line of the file
        for line in file:
            print(line)
    except FileNotFoundError:

        print(f, ' is not exists')
    finally:
        file.close()

if __name__ == '__main__':
    read_file('Transaction Log.txt')

#  how to write to the file


def write_data(file_name, text):
    file = open(file_name,'w')

    try:
        file.write(text)
    except IOError:
        print('Unable to create file on disk.')
    finally:
        file.close()


#  if __name__ == '__main__':
#    write_data('insertdata.txt', 'This is my sample text')