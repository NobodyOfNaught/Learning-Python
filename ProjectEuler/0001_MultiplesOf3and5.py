# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def totalofmultiples(number,max):
    multipleofX = number
    counter = 2
    result = 0
    while (multipleofX < max):
        result = result + multipleofX
        print(counter, multipleofX, result)
        multipleofX = number * counter
        counter += 1

    return result

totalsof3 = totalofmultiples(3,1000)
totalsof5 = totalofmultiples(5,1000)
totalsof15 = totalofmultiples(15,1000)

print(totalsof3 + totalsof5 - totalsof15)


