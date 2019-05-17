numbers = [1, 2, 3, 4, 5]

g = [3 * i for i in numbers]
print(g)
#  this is super important for data science
########################################################################
g1 = [3 * i for i in numbers if i < 2]
print(g1)

#  both of these do the same thing but the one above is much simpiler way to do it
# this type of coding is really only used for data science work
numbers1 = []
for i in range(len(numbers)):
    if numbers[i] < 2:
        numbers[i] *= 3
        numbers1.append(numbers[i])
print(numbers1)
##############################################################################

j = [[x, x ** 2] for x in numbers]
print(j)
