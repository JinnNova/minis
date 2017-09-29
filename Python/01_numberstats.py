# Not so useful Python minis by Hanna "Jinn" Enqvist

# A Program to find and calculate min, max, sum and mean of the given input numbers
summ = 0.0
minn = 0.0
maxx = 0.0
counter = 0
mean = 0.0

line = input("Give a number: ")
while line:
    line = float(line)

    if line > maxx:
        maxx = line
    #cant be elif or else. if user inputs only one number then min and max are the same
    if line < minn or minn == 0.0:
        minn = line

    summ = summ + line
    counter = counter + 1

    line = input("Give a number, or press enter to stop: ")

#if user does not input any numbers, we dont want to divide by 0
if counter != 0:
    mean = summ / counter

print("Minimum {0}, maximum {1}, sum {2} and mean {3}".format(minn, maxx, summ, mean))
