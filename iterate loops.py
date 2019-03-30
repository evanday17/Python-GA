# this will count the number of letters and numbers
word = "hello.world123"
digit_counter = 0
alpha_counter = 0

for i in word:
    if i.isdigit(): #checks if this is a digit or not....if true we add one to our digit counter
        digit_counter += 1
    elif i.isalpha():
        alpha_counter += 1 #checks if alpha...if true add one to our alpha counter
print('alpha ', alpha_counter)
print('digit', digit_counter)
