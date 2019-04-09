# for dictionaries the key (left side) has to be unique but the value can be anything

'''student = {
    "name": "Evan",
    "age": 29,
    "address": "1100 S broad"
}
print(student.items())

for key, value in student.items():
    print(key, " ", value)'''

student = {
    1: {
        "name": "Suresh",
        "age": 25
    },

    2:{
        "name": "evan",
        "age": 29
    },
    3: {
        "name": "nick",
        "age": 29
    }

}

for keys, values in student.items():
    for k, v in values.items():
            print(k, ":", v)